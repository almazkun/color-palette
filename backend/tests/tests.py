from django.test import TestCase


class TestSwatchesAPI(TestCase):
    def test_get_swatches_rgb(self):
        response = self.client.get("/api/v1/swatches/rgb/")

        self.assertEqual(response.status_code, 200)

        swatches = response.json()["swatches"]

        self.assertEqual(len(swatches), 5)

        for swatch in swatches:
            self.assertIn("color_space", swatch)
            self.assertIn("r", swatch)
            self.assertIn(swatch["r"], range(256))
            self.assertIn("g", swatch)
            self.assertIn(swatch["g"], range(256))
            self.assertIn("b", swatch)
            self.assertIn(swatch["b"], range(256))

    def test_get_swatches_hsl(self):
        response = self.client.get("/api/v1/swatches/hsl/")

        self.assertEqual(response.status_code, 200)

        swatches = response.json()["swatches"]

        self.assertEqual(len(swatches), 5)

        for swatch in swatches:
            self.assertIn("color_space", swatch)
            self.assertIn("h", swatch)
            self.assertIn(swatch["h"], range(361))
            self.assertIn("s", swatch)
            self.assertIn(swatch["s"], range(101))
            self.assertIn("l", swatch)
            self.assertIn(swatch["l"], range(101))

    def test_get_swatches_invalid(self):
        response = self.client.get("/api/v1/swatches/invalid/")

        self.assertEqual(response.status_code, 422)
        self.assertEqual(
            response.json(),
            {
                "detail": [
                    {
                        "ctx": {"expected": "'rgb' or 'hsl'"},
                        "loc": ["path", "color_space"],
                        "msg": "Input should be 'rgb' or 'hsl'",
                        "type": "enum",
                    }
                ]
            },
        )
