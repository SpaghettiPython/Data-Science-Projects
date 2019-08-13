drop table if exists master;
drop table if exists rt_100_df;
drop table if exists fandango_df;
drop table if exists rt_711_df;
drop table if exists rt_t10_df;


CREATE TABLE master (
Movie_Title varchar PRIMARY KEY,
Year int,
Director TEXT,
Genre varchar,
Content_Rating varchar,
Country varchar,
Budget int,
Gross_Box_Office int,
IMDB_Score float
);

CREATE TABLE RT_711_df (
Movie_Title varchar PRIMARY KEY,
Rotten_Tomatoes_Score float,
Audience_Score float	
);

CREATE TABLE fandango_df (
Movie_Title varchar PRIMARY KEY,
Rotten_Tomatoes_Score float,
Audience_Score float
);

CREATE TABLE RT_100_df (
Movie_Title varchar PRIMARY KEY,
Rotten_Tomatoes_Score float
);

CREATE TABLE RT_t10_df (
Movie_Title varchar PRIMARY KEY,
Rotten_Tomatoes_Score float,
Audience_Score float
);



