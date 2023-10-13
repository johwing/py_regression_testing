# Create or activate venv:
$venv = ".venv/py312"
if (!(Test-Path -Path $venv)) {
    python -m venv .venv/py312
}
.$venv\Scripts\Activate