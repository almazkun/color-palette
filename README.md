# color-palette
color-palette

# Prerequisites
It is easy to run with docker compose.
Other wise you need to have
- Python 3.12
- pipenv
- Node.js
- npm
- make (optional, there are some make commands)

Create .env file in the root directory and add the following variables:
```
echo "DJANGO_SECRET_KEY=your_secret_key" >> .env
echo "DJANGO_DEBUG=True" >> .env
echo "DJANGO_LOG_LEVEL=DEBUG" >> .env
echo "DJANGO_ALLOWED_HOSTS=localhost" >> .env
echo "DJANGO_CSRF_TRUSTED_ORIGINS=http://localhost:8000" >> .env
echo "DJANGO_CORS_ALLOWED_ORIGINS=http://localhost:3000" >> .env
```
# Run
```
docker compose up
```

# Frontend
Frontend is built with React. It is served on http://localhost:3000
It will show 5 lines of color palettes. You can click to regenerate the colors.

To start the frontend in development mode:
```
cd frontend
npm install
npm start
```

# Backend
Backend is built with Django. It is served on http://localhost:8000
It has a single endpoint to generate random color palettes.

To start the backend in development mode:
```
cd backend
cp .env.example .env
pipenv install
pipenv run python manage.py runserver
```

# Extensibility
To extend the color space support, following changes are needed:
- Frontend:
    - add a new color space option in the `COLOR_SPACES`
        - `HEX: 'hex'`
    - add a new color space option in the `formatColor` function
        - ```js
            case COLOR_SPACES.HEX:
                return `#${color.hex}`;
            ```
- Backend:
    - add a new color space in the `color.schemas.ColorSpace`
        - ```python
            class ColorSpace(str, Enum):
                RGB = "rgb"
                HSL = "hsl"
                HEX = "hex"
            ```
    - add a new Schema in the `color.schemas.py`
        - ```python
            class HEXColor(BaseColor):
                hex: str = Field(..., description="Hex value")
            ```
    - add a new schema in response schema
        - ```python
            class SwatchOutput(Schema):
                swatches: List[Union[RGBColor, HSLColor, HEXColor]]
            ```
    - add a new color generator in the `color.use_case.generate.py`
        - ```python
            def generate_hex():
                return {
                    "color_space": "hex",
                    "hex": "#%06x" % randint(0, 0xFFFFFF),
                }
            ```
    - register the color space and generator function:
        - ```python
            register_color_space("hex", generate_hex)
            ```
    - add a test case for new color space:
        - ```python
            elif swatch["color_space"] == "hex":
                self.assertIn("hex", swatch)
                self.assertRegex(swatch["hex"], r"^#[0-9a-f]{6}$")
            ```
    - Should work.