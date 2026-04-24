# VibeSurf has an Arbitrary File Write(RCE) via API


An authenticated arbitrary file write vulnerability exists in VibeSurf.

In repository version `0.5.18`, `vibe_surf/langflow/api/v2/files.py` reads a multipart filename directly from `file.filename` and passes it into the local storage layer, while `vibe_surf/langflow/services/storage/local.py` writes the resulting path using naive path concatenation without canonical containment checks. By obtaining a Bearer token either from `GET /api/v1/auto_login` or from `POST /api/v1/login` with the default credentials defined in `vibe_surf/langflow/services/settings/constants.py`, an authenticated attacker can submit a traversal filename to `POST /api/v2/files/` and cause VibeSurf to write arbitrary files outside the intended user storage directory. In the default Docker and docker-compose startup path, `vibe_surf/backend/main.py` enables auto-login by default, making this attack path reachable in the default deployment configuration.In realistic deployments, this can lead to Remote Code Execution (RCE).

I have placed the relevant malicious files, verification videos and PoC files in this repository.

