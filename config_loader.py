import json
import os

def load_env_config(path: str = "config.json"):
    """Loads local configuration for RPC and Jito nodes."""
    if not os.path.exists(path):
        return {"rpc": "https://api.mainnet-beta.solana.com", "jito": "mainnet.block-engine.jito.wtf"}
    
    with open(path, 'r') as f:
        return json.load(f)
