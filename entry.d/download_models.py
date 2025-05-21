import os
from huggingface_hub import snapshot_download
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HF_TOKEN")

MODELS = {
    "mbert.qry": "pythera/mbert-retrieve-qry-base",
    "mbert.ctx": "pythera/mbert-retrieve-ctx-base",
    "mbert.rerank": "pythera/mbert-rerank-base",
    "sati": "pythera/sati"
}

for name, repo in MODELS.items():
    print(f"⬇️ Downloading {name} from {repo}")
    snapshot_download(
        repo_id=repo,
        local_dir=f"./models/{name}/1",
        token=token,
        ignore_patterns=["*.safetensors", "*.pt"]
    )
