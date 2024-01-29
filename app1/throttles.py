from rest_framework.throttling import AnonRateThrottle,UserRateThrottle


class call_1_min(UserRateThrottle):
    scope = "one_per_min" #any name u want