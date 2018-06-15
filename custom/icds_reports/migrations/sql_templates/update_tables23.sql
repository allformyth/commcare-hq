ALTER TABLE ccs_record_monthly ADD COLUMN caste text;
ALTER TABLE ccs_record_monthly ADD COLUMN disabled text;
ALTER TABLE ccs_record_monthly ADD COLUMN minority text;
ALTER TABLE ccs_record_monthly ADD COLUMN resident text;
ALTER TABLE ccs_record_monthly ADD COLUMN anc_weight smallint;
ALTER TABLE ccs_record_monthly ADD COLUMN anc_blood_pressure smallint;
ALTER TABLE ccs_record_monthly ADD COLUMN bp_sys smallint;
ALTER TABLE ccs_record_monthly ADD COLUMN bp_dia smallint;
ALTER TABLE ccs_record_monthly ADD COLUMN anc_hemogloblin decimal;
ALTER TABLE ccs_record_monthly ADD COLUMN bleeding smallint;
ALTER TABLE ccs_record_monthly ADD COLUMN swelling smallint;
ALTER TABLE ccs_record_monthly ADD COLUMN blurred_vision smallint;
ALTER TABLE ccs_record_monthly ADD COLUMN convulsions smallint;
ALTER TABLE ccs_record_monthly ADD COLUMN rupture smallint;
ALTER TABLE ccs_record_monthly ADD COLUMN anemia smallint;
ALTER TABLE ccs_record_monthly ADD COLUMN eating_extra smallint;
ALTER TABLE ccs_record_monthly ADD COLUMN resting smallint;
ALTER TABLE ccs_record_monthly ADD COLUMN immediate_breastfeeding smallint;
ALTER TABLE ccs_record_monthly ADD COLUMN person_name text;
ALTER TABLE ccs_record_monthly ADD COLUMN edd date;
ALTER TABLE ccs_record_monthly ADD COLUMN delivery_nature smallint;
ALTER TABLE ccs_record_monthly ADD COLUMN is_ebf smallint;
ALTER TABLE ccs_record_monthly ADD COLUMN breastfed_at_birth smallint;
