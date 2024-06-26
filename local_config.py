
# ERPNext related configs
ERPNEXT_API_KEY = 'f6f9263ee33a5a6'
ERPNEXT_API_SECRET = '75ecd84e9c17638'
ERPNEXT_URL = 'https://5drs.erpfort.com'


# operational configs
PULL_FREQUENCY = 240 # in minutes
LOGS_DIRECTORY = 'logs' # logs of this script is stored in this directory
IMPORT_START_DATE = 20240101 # format: '20190501'

# Biometric device configs (all keys mandatory)
    #- device_id - must be unique, strictly alphanumerical chars only. no space allowed.
    #- ip - device IP Address
    #- punch_direction - 'IN'/'OUT'/'AUTO'/None
    #- clear_from_device_on_fetch: if set to true then attendance is deleted after fetch is successful.
                                    #(Caution: this feature can lead to data loss if used carelessly.)
devices = [
    {'device_id':'raqi','ip':'raqi-dv.dyndns.org', 'punch_direction': 'Auto', 'clear_from_device_on_fetch': False},
    {'device_id':'5drs','ip':'5drs.dyndns.org', 'punch_direction': 'Auto', 'clear_from_device_on_fetch': False}
]

# Configs updating sync timestamp in the Shift Type DocType
# please, read this thread to know why this is necessary https://discuss.erpnext.com/t/v-12-hr-auto-attendance-purpose-of-last-sync-of-checkin-in-shift-type/52997
shift_type_device_mapping = [
    {'shift_type_name': ['Shift1'], 'related_device_id': ['test_1','test_2']}
]


# Ignore following exceptions thrown by ERPNext and continue importing punch logs.
# Note: All other exceptions will halt the punch log import to erpnext.
#       1. No Employee found for the given employee User ID in the Biometric device.
#       2. Employee is inactive for the given employee User ID in the Biometric device.
#       3. Duplicate Employee Checkin found. (This exception can happen if you have cleared the logs/status.json of this script)
# Use the corresponding number to ignore the above exceptions. (Default: Ignores all the listed exceptions)
allowed_exceptions = [1,2,3]
