DROP TABLE IF EXISTS prescribers;

CREATE TABLE prescribers (
npi	TEXT,
nppes_provider_last_org_name TEXT,
nppes_provider_first_name TEXT,
nppes_provider_city TEXT,
nppes_provider_state TEXT,
specialty_description TEXT,
description_flag TEXT,
drug_name	TEXT,
generic_name	TEXT,
bene_count	INTEGER,
total_claim_count	FLOAT,
total_30_day_fill_count	FLOAT,
total_day_supply 	FLOAT,
total_drug_cost		FLOAT,
bene_count_ge65		INTEGER,
bene_count_ge65_suppress_flag	TEXT,
total_claim_count_ge65	FLOAT,
ge65_suppress_flag	TEXT,
total_30_day_fill_count_ge65	FLOAT,
total_day_supply_ge65	FLOAT,
total_drug_cost_ge65	FLOAT
);

\copy prescribers FROM 'provider.csv' csv header