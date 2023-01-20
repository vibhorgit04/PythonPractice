from utilities.configurations import getConfig

class getProperties:
            getappurl = getConfig()['API']['endpoint']
            getappurll = getConfig()['APILOCAL']['endpoint']
            getheaders = getConfig()['API']['headers']
            getDbHostname = getConfig()['SQL']['host']
            getDbUser = getConfig()['SQL']['user']
            getDbPass = getConfig()['SQL']['password']
            getDbName = getConfig()['SQL']['database']
