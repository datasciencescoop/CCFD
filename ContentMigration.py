import logging
import time
import os
import json
from mstrio.object_management.migration import (
    bulk_full_migration,
    bulk_migrate_package,
    Migration,
    PackageConfig,
    PackageContentInfo,
    PackageSettings
)

from mstrio.types import ObjectTypes

from mstrio.users_and_groups.user import User

from mstrio.connection import get_connection

from mstrio.modeling.schema import (
    Attribute,
    AttributeDisplays,
    AttributeForm,
    AttributeSort,
    AttributeSorts,
    DataType,
    FormReference,
    list_attributes,
    list_facts,
    ObjectSubType,
    Relationship,
    SchemaManagement,
    SchemaObjectReference,
    SchemaUpdateType
)


from mstrio.object_management import (
    Folder,
    full_search,
    get_my_personal_objects_contents,
    get_predefined_folder_contents,
    get_search_results,
    get_search_suggestions,
    list_folders,
    list_objects,
    Object,
    PredefinedFolders,
    quick_search,
    quick_search_from_object,
    SearchObject,
    SearchPattern,
    SearchResultsFormat,
    start_full_search
)

from mstrio.modeling import (
    DataType,
    DefaultSubtotals,
    Dimensionality,
    DimensionalityUnit,
    FormatProperty,
    list_metrics,
    Metric,
    MetricFormat,
    ObjectSubType,
    SchemaManagement,
    SchemaObjectReference,
    SchemaUpdateType
)

from mstrio.project_objects import list_olap_cubes, OlapCube
from mstrio.connection import get_connection, Connection
from mstrio.connection import get_connection


import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


ENV_VARS = ['ACTION', 'TENANT', 'URL', 'USERNAME', 'PASSWORD', 'APP']

for var in ENV_VARS:
    if var not in os.environ:
        raise ValueError(f"Required environment variable '{var}' is missing.")


# Logging
logging.basicConfig(level=logging.INFO)

# Constants
REFRESH_JOB_TRIGGERED = 'Refresh Job Triggered'
MIGRATION_JOB_TRIGGERED = 'Migration Job Triggered'
INVALID_OPTION = 'Invalid Option'


action = os.environ['ACTION']

if action == 'refresh':
    logging.info(REFRESH_JOB_TRIGGERED)
elif action == 'migration':
    logging.info(MIGRATION_JOB_TRIGGERED)
else:
    logging.info(INVALID_OPTION)
