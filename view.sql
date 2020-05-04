CREATE OR REPLACE VIEW season_info AS
SELECT DISTINCT
season.season_year,
season.winner_name,
winner.total_wins,
season.top_scorer_name,
top_scorer.total_goals,
season.goals
FROM
season
INNER JOIN top_scorer ON season.top_scorer_name=top_scorer.top_scorer_name
INNER JOIN winner ON season.winner_name=winner.winner_name;
