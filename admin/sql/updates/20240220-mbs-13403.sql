\set ON_ERROR_STOP 1

BEGIN;

ALTER TABLE link_type DROP COLUMN priority CASCADE;

COMMIT;