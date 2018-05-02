import time, datetime, pytz
from datetime import tzinfo


class GreenTime(object):
    calendar = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
                6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October',
                11: 'November', 12: 'December'}

    def __init__(self, gtime=None, is_k=False, allow_dec=True, **kwargs):
        """
        init GreetTime obj
        input current time(gtime) and specific format. e.g 1514736000, 1514736000000
        :param gtime: specified time or generate current time
        :param is_k: g_time's timestamp format for javascript or java... , like 1514736000000
        :param allow_dec: g_time's timestamp format for python, swift... , like 1514736000.000 , is mutex with arguments is_k
        :param kwargs: can use tz=pytz.timezone('country/city')
        """

        if not gtime:
            gtime = time.time()

        else:
            if not isinstance(gtime, float) and not isinstance(gtime, int):
                raise Exception("gtime is not a number type")

        if is_k:
            self.green_time = gtime / 1000
            self.is_thousand = is_k
        else:
            self.green_time = gtime
            self.is_thousand = is_k

        self.have_millisecond = allow_dec
        if not allow_dec:
            self.green_time = int(self.green_time)

        tz = kwargs.get('tz')
        self.tz = tz if isinstance(tz, tzinfo) else None
        self.green_datetime = datetime.datetime.fromtimestamp(self.green_time, tz=self.tz)

        self.green_year = self.green_datetime.year
        self.green_month = self.green_datetime.month
        self.green_day = self.green_datetime.day
        self.green_hour = self.green_datetime.hour
        self.green_minute = self.green_datetime.minute
        self.green_second = self.green_datetime.second
        self.green_millisecond = self.green_datetime.microsecond
        self.green_week = self.green_datetime.weekday()

        if self.tz:
            mid_date = self.tz.localize(
                datetime.datetime(self.green_year, self.green_month, self.green_day, 0, 0, 0))
        else:
            mid_date = datetime.datetime(self.green_year, self.green_month, self.green_day, 0, 0, 0)
        self.green_midnight = mid_date.timestamp()

    def __repr__(self):
        return str(self.green_time * ((1000 if self.is_thousand else False) or 1))

    def get_datetime(self):
        """
        datetime format
        :return: datetime
        """
        return self.green_datetime

    def year(self):
        return self.green_year

    def month(self):
        return self.green_month

    def day(self):
        return self.green_day

    def hour(self):
        return self.green_hour

    def minute(self):
        return self.green_minute

    def second(self):
        return self.green_second

    def week(self):
        return self.green_week

    def midnight(self):
        """
        middle night
        :return: int
        """
        mid_date = self.green_midnight
        if not self.have_millisecond:
            mid_date = int(mid_date)
        if self.is_thousand:
            mid_date *= 1000
        return mid_date

    def gtime(self, take_k=False):
        """
        get green time by timestamp
        :param take_k: bool
        :return: int
        """

        k_weight = 1000 if self.is_thousand or take_k else 1

        return int(self.green_time * k_weight)

    def plus(self, hour=0, minute=0, second=0):
        """
        add time and change self default time
        :param hour: int
        :param minute: int
        :param second: int
        :return: int
        """
        k_weight = 1000 if self.is_thousand else 1
        new_time = ((3600 * hour + 60 * minute + second) + self.green_time) * k_weight

        self.__init__(new_time, is_k=self.is_thousand, allow_dec=self.have_millisecond)
        return self.gtime(take_k=self.is_thousand)

    def subtract(self, hour=0, minute=0, second=0):
        """
        subtract time and change self default time
        :param hour: int
        :param minute: int
        :param second: int
        :return: int
        """
        k_weight = 1000 if self.is_thousand else 1
        new_time = (self.green_time - (3600 * hour + 60 * minute + second)) * k_weight

        self.__init__(new_time, is_k=self.is_thousand, allow_dec=self.have_millisecond)
        return self.gtime(take_k=self.is_thousand)

    def after(self, hour=0, minute=0, second=0):
        """
        create GreenTime obj which base on self and after by specified time
        :param hour: int
        :param minute: int
        :param second: int
        :return: GreenTime()
        """
        new_time = (self.green_time + (3600 * hour + 60 * minute + second)) * (
            (1000 if self.is_thousand else False) or 1)
        return GreenTime(new_time, is_k=self.is_thousand, allow_dec=self.have_millisecond, tz=self.tz)

    def before(self, hour=0, minute=0, second=0):
        """
        create GreenTime obj which base on self and before by specified time
        :param hour: int
        :param minute: int
        :param second: int
        :return: GreenTime()
        """
        new_time = (self.green_time - (3600 * hour + 60 * minute + second)) * (
            (1000 if self.is_thousand else False) or 1)
        return GreenTime(new_time, is_k=self.is_thousand, allow_dec=self.have_millisecond, tz=self.tz)

    @staticmethod
    def mk_time(year=1970, month=1, day=1, hour=0, minute=0, second=0):
        """
        quickly make timestamp by specified time
        :param year: int
        :param month: int
        :param day: int
        :param hour: int
        :param minute: int
        :param second: int
        :return: int
        """
        return time.mktime(
            datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second).timetuple())

    @staticmethod
    def mk_gtime(allow_dec=True, year=1970, month=1, day=1, hour=0, minute=0, second=0, **kwargs):
        return GreenTime(time.mktime(
            datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second).timetuple()),
            is_k=False, allow_dec=allow_dec, **kwargs)

    @staticmethod
    def now(allow_dec=True, take_k=False, **kwargs):
        g_now = GreenTime(time.time(), allow_dec=allow_dec, is_k=take_k, **kwargs)
        return g_now.gtime(take_k=take_k)

    @staticmethod
    def green_now(allow_dec=True, take_k=False, **kwargs):
        return GreenTime(time.time(), allow_dec=allow_dec, is_k=take_k, **kwargs)
