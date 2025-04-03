import os
import unittest
import traceback
from run import app
from werkzeug.routing import BuildError

class TestAllPages(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        self.service_area_data_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'app', 'templates', 'service_areas', 'data')
        )

    def get_service_area_urls(self):
        urls = []
        if os.path.exists(self.service_area_data_dir):
            for filename in os.listdir(self.service_area_data_dir):
                if filename.endswith('.json'):
                    area_name = filename[:-5].replace('_', '-')
                    urls.append(f'/service-areas/{area_name}')
        return urls

    def test_all_pages(self):
        static_urls = [
            '/', '/about-us', '/privacy-policy', '/contact', '/testimonials',
            '/services/baby-blessings', '/services/baptisms', '/services/celebrations',
            '/services/naming-ceremonies', '/services/gallery', '/services/services',
            '/service_areas/service_areas', '/service_areas/location_templates'
        ]

        all_urls = static_urls + self.get_service_area_urls()

        errors = {}

        for url in all_urls:
            try:
                response = self.client.get(url)
                if response.status_code != 200:
                    errors[url] = f"Status code: {response.status_code}"
            except Exception as e:
                tb = traceback.format_exc()
                errors[url] = f"Exception:\n{tb}"

        if errors:
            error_log = "\n\n".join([f"{url}:\n{msg}" for url, msg in errors.items()])
            self.fail(f"\n\nErrors found in route tests:\n\n{error_log}")
        else:
            print("✅ All pages passed.")

if __name__ == '__main__':
    unittest.main()
