CREATE TABLE  season 
(
season_year NUMBER(38) NOT NULL 
);
ALTER TABLE  season
  ADD CONSTRAINT season_pk PRIMARY KEY (season_year);

INSERT INTO season(season_year)
VALUES('1929');

INSERT INTO season(season_year)
VALUES('1930');

INSERT INTO season(season_year)
VALUES('1931');

INSERT INTO season(season_year)
VALUES('1932');

INSERT INTO season(season_year)
VALUES('1933');


CREATE TABLE team
(
team_name varchar(50) NOT NULL
);
ALTER TABLE  team
  ADD CONSTRAINT team_pk PRIMARY KEY (team_name);
  
  INSERT INTO team(team_name)
VALUES('Barcelona');
  
  INSERT INTO team(team_name)
VALUES('Real Madrid');

    INSERT INTO team(team_name)
VALUES('Athletic Bilbao');
  
    INSERT INTO team(team_name)
VALUES('Atletico Aviacion [A]');
  
    INSERT INTO team(team_name)
VALUES('Atletico Aviacion');
  
  


CREATE TABLE team_season_winner
(
team_name_fk VARCHAR(50) ,
season_year_fk NUMBER(38)
);
ALTER TABLE  team_season_winner
  ADD CONSTRAINT team_season_winner_pk PRIMARY KEY (team_name_fk, season_year_fk);  
ALTER TABLE team_season_winner
  ADD CONSTRAINT season1_pk FOREIGN KEY (season_year_fk) REFERENCES season (season_year);
ALTER TABLE  team_season_winner
  ADD CONSTRAINT team1_pk FOREIGN KEY (team_name_fk) REFERENCES team (team_name);

 INSERT INTO team_season_winner(team_name_fk,season_year_fk)
VALUES('Barcelona','1929');

 INSERT INTO team_season_winner(team_name_fk,season_year_fk)
VALUES('Athletic Bilbao','1930');

 INSERT INTO team_season_winner(team_name_fk,season_year_fk)
VALUES('Athletic Bilbao','1931');

 INSERT INTO team_season_winner(team_name_fk,season_year_fk)
VALUES('Real Madrid','1932');

 INSERT INTO team_season_winner(team_name_fk,season_year_fk)
VALUES('Real Madrid','1933');


create table human
(
human_name varchar(50) NOT NULL
);
ALTER TABLE  human
  ADD CONSTRAINT human_pk PRIMARY KEY (human_name);
  
  INSERT INTO human(human_name)
VALUES('Paco Bienzobas');

  INSERT INTO human(human_name)
VALUES('Guillermo Gorostiza');

INSERT INTO human(human_name)
VALUES('Agustin Sauto Arana');

INSERT INTO human(human_name)
VALUES('Manuel Olivares');

create table human_season(
human_name_fk varchar(50),
season_year_fk NUMBER(38)
);
ALTER TABLE  human_season
  ADD CONSTRAINT human_season_pk PRIMARY KEY (human_name_fk, season_year_fk);  
ALTER TABLE human_season
  ADD CONSTRAINT season2_pk FOREIGN KEY (season_year_fk) REFERENCES season (season_year);
ALTER TABLE  human_season
  ADD CONSTRAINT human1_pk FOREIGN KEY (human_name_fk) REFERENCES human (human_name);
  
  INSERT INTO human_season(human_name_fk,season_year_fk )
VALUES('Paco Bienzobas', '1929');

  INSERT INTO human_season(human_name_fk,season_year_fk )
VALUES('Guillermo Gorostiza', '1930');

  INSERT INTO human_season(human_name_fk,season_year_fk )
VALUES('Agustin Sauto Arana', '1931');

 INSERT INTO human_season(human_name_fk,season_year_fk )
VALUES('Guillermo Gorostiza', '1932');

 INSERT INTO human_season(human_name_fk,season_year_fk )
VALUES('Manuel Olivares', '1933');

