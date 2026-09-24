import unittest

from app import app


class TimeApplicationTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index_points_to_time_endpoint(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("/time", response.get_json()["message"])

    def test_time_returns_utc_timestamp(self):
        response = self.client.get("/time")
        payload = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(payload["timezone"], "UTC")
        self.assertTrue(payload["current_time"].endswith("Z"))


if __name__ == "__main__":
    unittest.main()
