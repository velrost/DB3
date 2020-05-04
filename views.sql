  
CREATE  VIEW season_info1 AS
SELECT DISTINCT
season.season_year,
human_season.human_name_fk,
team_season_winner.team_name_fk
FROM
season
INNER JOIN human_season ON season.season_year=human_season.season_year_fk
INNER JOIN team_season_winner ON season.season_year=team_season_winner.season_year_fk;

  