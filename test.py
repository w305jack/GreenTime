import unittest
import pytz
from green_time import GreenTime


class GreenTimeTestCase(unittest.TestCase):
    def setUp(self):
        self.tz = pytz.timezone('Asia/Taipei')

    def test_green_time(self):
        green_time = GreenTime(gtime=1514736000)  # 2018/1/1 00:00:00
        self.assertEqual(green_time.gtime(), 1514736000.0)
        self.assertEqual(green_time.gtime(take_k=True), 1514736000000)
        self.assertEqual(green_time.year(), 2018)
        self.assertEqual(green_time.month(), 1)
        self.assertEqual(green_time.day(), 1)
        self.assertEqual(green_time.hour(), 0)
        self.assertEqual(green_time.minute(), 0)
        self.assertEqual(green_time.second(), 0)
        self.assertEqual(green_time.midnight(), 1514736000)


    def test_mk_gtime(self):
        mk_gtime = GreenTime.mk_gtime(year=2018, month=1, day=1, hour=0, minute=0, second=0, tz=self.tz)
        self.assertIsInstance(mk_gtime, GreenTime)
        self.assertEqual(mk_gtime.gtime(), 1514736000.0)

        mk_gtime = GreenTime.mk_gtime(allow_dec=False, year=2018, month=1, day=1, hour=0, minute=0, second=0,
                                      tz=self.tz)
        self.assertIsInstance(mk_gtime, GreenTime)
        self.assertEqual(mk_gtime.gtime(), 1514736000)
        self.assertEqual(mk_gtime.gtime(take_k=True), 1514736000000)

    def test_mk_time(self):
        mk_time = GreenTime.mk_time(year=2018, month=1, day=1, hour=0, minute=0, second=0)
        self.assertIsInstance(mk_time, float)
        self.assertEqual(mk_time, 1514736000.0)

    def test_after(self):
        green_time = GreenTime(gtime=1514736000)
        after = green_time.after(hour=1, minute=1, second=1)
        self.assertIsInstance(after, GreenTime)
        self.assertEqual(after.gtime(), 1514736000 + (3600 + 60 + 1))

    def test_before(self):
        green_time = GreenTime(gtime=1514736000)
        before = green_time.before(hour=1, minute=1, second=1)
        self.assertIsInstance(before, GreenTime)
        self.assertEqual(before.gtime(), 1514736000 - (3600 + 60 + 1))

    def test_plus(self):
        green_time = GreenTime(gtime=1514736000)
        green_time.plus(hour=1, minute=1, second=1)
        self.assertEqual(green_time.gtime(), 1514736000 + (3600 + 60 + 1))
        self.assertEqual(green_time.hour(), 1)
        self.assertEqual(green_time.minute(), 1)
        self.assertEqual(green_time.second(), 1)

    def test_subtract(self):
        green_time = GreenTime(gtime=1514736000)
        green_time.subtract(hour=1, minute=1, second=1)  # 2017/12/31 22:58:59
        self.assertEqual(green_time.gtime(), 1514736000 - (3600 + 60 + 1))
        self.assertEqual(green_time.hour(), 22)
        self.assertEqual(green_time.minute(), 58)
        self.assertEqual(green_time.second(), 59)


if __name__ == '__main__':
    unittest.main()
