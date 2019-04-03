import configparser

from requests.auth import HTTPBasicAuth
from requests import Session

from zeep import Client, Settings
from zeep.transports import Transport


class TimrApi():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.identifier = self.config['Auth']['identifier']
        self.token = self.config['Auth']['token']
        self.session = Session()
        self.session.auth = HTTPBasicAuth(self.identifier, self.token)
        self.settings = Settings(strict=False)
        self.client = Client(wsdl='https://timrsync.timr.com/timr/timrsync.wsdl',
                             transport=Transport(session=self.session), settings=self.settings)

    def get_cars(self):
        return self.client.service.GetCars()

    def get_users(self):
        return self.client.service.GetUsers()

    def get_admins(self):
        return [user for user in self.get_users() if user.isAdmin == True]

    def get_projecttimes(self):
        return self.client.service.GetProjectTimes()

    def get_running_projecttimes(self):
        return self.client.service.GetRunningProjectTimes()

    def get_user_projecttimes(self, externalUserID):
        return [item for item in self.get_projecttimes() if item.externalUserId == externalUserID]

    def get_worktimes(self):
        return self.client.service.GetWorkTimes()

    def get_running_worktimes(self):
        return self.client.service.GetRunningWorkTimes()

    def get_user_worktimes(self, externalUserID):
        return [item for item in self.get_worktimes() if item.externalUserId == externalUserID]

    def get_drivelogs(self):
        return self.client.service.GetDriveLogs()

    def get_user_drivelogs(self, externalUserID):
        return [item for item in self.get_drivelogs() if item.externalUserId == externalUserID]

    def get_workitems(self):
        return self.client.service.GetWorkItems()

    def get_Tasks(self):
        return self.client.service.GetTasks()

    def filter_by_weeknumber(self, items, start, end):
        if start > end:
            raise ValueError('Start can not be bigger than end.')
        elif end > 52:
            raise ValueError('A Year only has 52 weeks.')

        return [item for item in items if
                int(item.startTime.strftime('%W')) + 1 >= start and int(item.startTime.strftime('%W')) + 1 <= end]

    def filter_by_month(self, items, year, month):
        return [item for item in items if item.startTime.year == year and item.startTime.month == month]