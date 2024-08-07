FIELD = "FIELD"
NOTIFICATION_FOR_USER = "NOTIFICATION_FOR_USER"

DEFAULT_TYPE = [
    (FIELD, "Field"),
    (NOTIFICATION_FOR_USER, "Notification for users"),
]

STRING = "STRING"
INTEGER = "INTEGER"
FLOAT = "FLOAT"
HTML = "HTML"

FIELD_TYPE = [
    (STRING, "String"),
    (INTEGER, "Integer"),
    (FLOAT, "Float"),
    (HTML, "Html"),
]

NOTIFICATION_FOR_APPROVED = "NOTIFICATION_FOR_APPROVED"
PREPARE_FOR_INSPECTION_PLAN = "PREPARE_FOR_INSPECTION_PLAN"
NEED_REAL_DATE_FOR_INSPECTION_PLAN = "NEED_REAL_DATE_FOR_INSPECTION_PLAN"

NOTIFICATION_TYPE = [
    (NOTIFICATION_FOR_APPROVED, NOTIFICATION_FOR_APPROVED),
    (PREPARE_FOR_INSPECTION_PLAN, PREPARE_FOR_INSPECTION_PLAN),
    (NEED_REAL_DATE_FOR_INSPECTION_PLAN, NEED_REAL_DATE_FOR_INSPECTION_PLAN),
]


FIXABLE = "FIXABLE"
UNFIXABLE = "UNFIXABLE"
PENDING = "PENDING"

REPAIR_STATUS = [
    (PENDING, "Pending"),
    (FIXABLE, "Fixable"),
    (UNFIXABLE, "Unfixable"),
]

REPAIR_PROCESSING = "REPAIR_PROCESSING"
REPAIR = "REPAIR"
NEW_CASTING = "NEW_CASTING"

TECHNICAL_INCIDENT_METHOD = [
    (REPAIR_PROCESSING, "Repair processing"),
    (REPAIR, "Repair"),
    (NEW_CASTING, "New casting"),
]

MACHINERY = "MACHINERY"
BOONG = "BOONG"

DEPARTMENT_IN_CHARGE = [
    (MACHINERY, "Machinery"),
    (BOONG, "Boong"),
]

APPROVED_HANDBOOK_SECTION_VERSION = "APPROVED_HANDBOOK_SECTION_VERSION"
REJECTED_HANDBOOK_SECTION_VERSION = "REJECTED_HANDBOOK_SECTION_VERSION"
PENDING_HANDBOOK_SECTION_VERSION = "PENDING_HANDBOOK_SECTION_VERSION"

SECTION_FOR_HANDBOOK = "SECTION_FOR_HANDBOOK"
SECTION_FOR_PARENT_SECTION = "SECTION_FOR_PARENT_SECTION"
