import src.scripts.setup_cfg as cfg
import src.scripts.install_req as req

def run_init_task():
    # First setup config, it also checks if user first launch
    cfg.setup_cfg()
    req.install_req()