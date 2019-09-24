function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel
  // Use `d3.json` to fetch the metadata for a sample
  const metadataURL = `/metadata/${sample}`;
  // Use d3 to select the panel with id of `#sample-metadata`
    d3.json(metadataURL).then(function(sample){
      const sampleData = d3.select(`#sample-metadata`);
      // Use `.html("") to clear any existing metadata
    sampleData.html("");
  // Use `Object.entries` to add each key and value pair to the panel
  // Hint: Inside the loop, you will need to use d3 to append new
  // tags for each key-value in the metadata.
    Object.entries(sample).forEach(function([key,value]){
      const row = sampleData.append("p");
      row.text(`${key}:${value}`)
    })
  });
}



function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  const plotD = `/samples/${sample}`;
  // @TODO: Build a Bubble Chart using the sample data
    d3.json(plotD).then(function(data){
      const bubbles = {
        x: data.otu_ids,
        y: data.sample_values,
        mode: `markers`,
        text: data.otu_labels,
        marker: {
          size: data.sample_values,
          color: data.otu_ids
        }
      };
      const data4 = [bubbles];
      const layout = {
        title: "Belly Bact",
        xaxis: {title: "OTU ID"}
      };
      Plotly.newPlot("bubble", data4, layout);

      // @TODO: Build a Pie Chart

    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
      d3.json(plotD).then(function(data){
        const data1 = [{
          values: data.sample_values.slice(0, 10),
          lables: data.otu_ids.slice(0, 10),
          hovertext: data.otu_labels.slice(0,10),
          type: "pie"
        }];
        Plotly.newPlot('pie', data1);
    });
  });
}

function init() {
  // Grab a reference to the dropdown select element
  let selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
