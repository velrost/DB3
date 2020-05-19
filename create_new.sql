CREATE TABLE  season 
(
season_year VARCHAR(50) NOT NULL 
);
ALTER TABLE  season
  ADD CONSTRAINT season_pk PRIMARY KEY (season_year);


CREATE TABLE team
(
team_name varchar(50) NOT NULL
);
ALTER TABLE  team
  ADD CONSTRAINT team_pk PRIMARY KEY (team_name);



CREATE TABLE team_season_winner
(
team_name_fk VARCHAR(50) ,
season_year_fk VARCHAR(50)
); 
ALTER TABLE team_season_winner
  ADD CONSTRAINT season1_pk FOREIGN KEY (season_year_fk) REFERENCES season (season_year);
ALTER TABLE  team_season_winner
  ADD CONSTRAINT team1_pk FOREIGN KEY (team_name_fk) REFERENCES team (team_name);



create table human
(
human_name varchar(50) NOT NULL
);
ALTER TABLE  human
  ADD CONSTRAINT human_pk PRIMARY KEY (human_name);



create table human_season(
human_name_fk varchar(50),
season_year_fk VARCHAR(50)
);
ALTER TABLE human_season
  ADD CONSTRAINT season2_pk FOREIGN KEY (season_year_fk) REFERENCES season (season_year);
ALTER TABLE  human_season
  ADD CONSTRAINT human1_pk FOREIGN KEY (human_name_fk) REFERENCES human (human_name);