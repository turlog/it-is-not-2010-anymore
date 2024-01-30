import requests


for result in requests.get(
    "https://report-editor-plab.apps.dev-01.us-central1.dev.sabre-gcp.com/api/v0/test/102824/result"
).json():
    match result:
        case {
            "assessment": ("fail" | "warning") as assessment,
            "name": name,
            "value": float(value),
            "unit": (str() | None) as unit,
            "pac": [*pac, _],
        } if len(pac) > 0 and "JVM" in name:
            print(
                f"{name} = {value:g} {f'{unit} ' if unit else ''}-> {assessment.upper()}"
            )
