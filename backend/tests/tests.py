from django.test import TestCase


class TestSwatchesAPI(TestCase):
    def test_get_swatches(self):
        response = self.client.get("/api/v1/swatches/")

        self.assertEqual(response.status_code, 200)

        swatches = response.json()["swatches"]

        self.assertEqual(len(swatches), 5)

        for swatch in swatches:
            if swatch["color_space"] == "rgb":
                self.assertIn("r", swatch)
                self.assertIn(swatch["r"], range(256))
                self.assertIn("g", swatch)
                self.assertIn(swatch["g"], range(256))
                self.assertIn("b", swatch)
                self.assertIn(swatch["b"], range(256))
            elif swatch["color_space"] == "hsl":
                self.assertIn("h", swatch)
                self.assertIn(swatch["h"], range(361))
                self.assertIn("s", swatch)
                self.assertIn(swatch["s"], range(101))
                self.assertIn("l", swatch)
                self.assertIn(swatch["l"], range(101))
            elif swatch["color_space"] == "hex":
                self.assertIn("hex", swatch)
                self.assertRegex(swatch["hex"], r"^#[0-9a-f]{6}$")
