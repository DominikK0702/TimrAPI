from requests.auth import HTTPBasicAuth
from requests import Session

from zeep import Client, Settings
from zeep.transports import Transport


class TimrApi():
    def __init__(self):
        self.identifier = 'identifier'
        self.token = 'token'
        self.session = Session()
        self.session.auth = HTTPBasicAuth(self.identifier, self.token)
        self.settings = Settings(strict=False)
        self.client = Client(wsdl='https://timrsync.timr.com/timr/timrsync.wsdl',
                             transport=Transport(session=self.session), settings=self.settings)

    def AddCar(self):
        raise NotImplementedError

    def AddTask(self):
        raise NotImplementedError

    def AddUser(self):
        raise NotImplementedError

    def AddWorkItem(self):
        raise NotImplementedError

    def AssignCarToUser(self):
        raise NotImplementedError

    def AssignTaskToUser(self):
        raise NotImplementedError

    def DeleteCar(self):
        raise NotImplementedError

    def DeleteCarByUUID(self):
        raise NotImplementedError

    def DeleteTask(self):
        raise NotImplementedError

    def DeleteTaskByUUID(self):
        raise NotImplementedError

    def DeleteUser(self):
        raise NotImplementedError

    def DeleteUserByUUID(self):
        raise NotImplementedError

    def DeleteWorkItem(self):
        raise NotImplementedError

    def DeleteWorkItemByUUID(self):
        raise NotImplementedError

    def GetCars(self):
        return self.client.service.GetCars()

    def GetDriveLogs(self):
        return self.client.service.GetDriveLogs()

    def GetProjectTimes(self):
        return self.client.service.GetProjectTimes()

    def GetRunningDriveLogs(self):
        return self.client.service.GetRunningDriveLogs()

    def GetRunningProjectTimes(self):
        return self.client.service.GetRunningProjectTimes()

    def GetRunningWorkTimes(self):
        return self.client.service.GetRunningWorkTimes()

    def GetTask(self, externalid):
        return self.client.service.GetTask(externalid)

    def GetTaskByUUID(self, uuid):
        return self.client.service.GetTaskByUUID(uuid)

    def GetTasks(self):
        return self.client.service.GetTasks()

    def GetUsers(self):
        return self.client.service.GetUsers()

    def GetWorkItems(self):
        return self.client.service.GetWorkItems()

    def GetWorkTimes(self):
        return self.client.service.GetWorkTimes()

    def LockProjectTimes(self):
        raise NotImplementedError

    def RemoveCarFromUser(self):
        raise NotImplementedError

    def RemoveTaskFromUser(self):
        raise NotImplementedError

    def SaveDriveLog(self):
        raise NotImplementedError

    def SaveProjectTime(self):
        raise NotImplementedError

    def SaveWorkTime(self):
        raise NotImplementedError

    def SetDriveLogsStatus(self):
        raise NotImplementedError

    def SetProjectTimesStatus(self):
        raise NotImplementedError

    def SetTaskExternalId(self):
        raise NotImplementedError

    def SetWorkTimesStatus(self):
        raise NotImplementedError

    def UnlockProjectTimes(self):
        raise NotImplementedError

    def UpdateCar(self):
        raise NotImplementedError

    def UpdateCarId(self):
        raise NotImplementedError

    def UpdateTask(self):
        raise NotImplementedError

    def UpdateTaskId(self):
        raise NotImplementedError

    def UpdateUser(self):
        raise NotImplementedError

    def UpdateUserId(self):
        raise NotImplementedError

    def UpdateWorkItem(self):
        raise NotImplementedError

    def UpdateWorkItemId(self):
        raise NotImplementedError
