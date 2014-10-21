from confu.ansible import S3LookupModule


class LookupModule(S3LookupModule):

    bucket_var = 'citadel_bucket'

    profile_var = 'citadel_profile'

    region_var = 'citadel_region'

    cache = {}
