from argparse import ArgumentParser, Namespace

import torch

from accelerate.utils import set_seed
from utils.inference import (
    V1InferenceLoop,
    BSRInferenceLoop, BFRInferenceLoop, BIDInferenceLoop, UnAlignedBFRInferenceLoop
)


def check_device(device: str) -> str:
    if device == "cuda":
        if not torch.cuda.is_available():
            print("CUDA not available because the current PyTorch install was not "
                  "built with CUDA enabled.")
            device = "cpu"
    else:
        if device == "mps":
            if not torch.backends.mps.is_available():
                if not torch.backends.mps.is_built():
                    print("MPS not available because the current PyTorch install was not "
                          "built with MPS enabled.")
                    device = "cpu"
                else:
                    print("MPS not available because the current MacOS version is not 12.3+ "
                          "and/or you do not have an MPS-enabled device on this machine.")
                    device = "cpu"
    print(f"using device {device}")
    return device


def parse_args_from_dict(params: dict) -> Namespace:
    parser = ArgumentParser()
    ### model parameters
    parser.add_argument("--task", type=str, default="fr", choices=["sr", "dn", "fr", "fr_bg"])
    parser.add_argument("--upscale", type=float, default=2.0)
    parser.add_argument("--version", type=str, default="v2", choices=["v1", "v2"])
    ### sampling parameters
    parser.add_argument("--steps", type=int, default=50)
    parser.add_argument("--better_start", action="store_true")
    parser.add_argument("--tiled", action="store_true")
    parser.add_argument("--tile_size", type=int, default=512)
    parser.add_argument("--tile_stride", type=int, default=256)
    parser.add_argument("--pos_prompt", type=str, default="")
    parser.add_argument("--neg_prompt", type=str,
                        default="low quality, blurry, low-resolution, noisy, unsharp, weird textures")
    parser.add_argument("--cfg_scale", type=float, default=4.0)
    ### input parameters
    parser.add_argument("--input", type=str, default="inputs/demo/bfr/aligned")
    parser.add_argument("--n_samples", type=int, default=1)
    ### guidance parameters
    parser.add_argument("--guidance", action="store_true")
    parser.add_argument("--g_loss", type=str, default="w_mse", choices=["mse", "w_mse"])
    parser.add_argument("--g_scale", type=float, default=0.0)
    parser.add_argument("--g_start", type=int, default=1001)
    parser.add_argument("--g_stop", type=int, default=-1)
    parser.add_argument("--g_space", type=str, default="latent")
    parser.add_argument("--g_repeat", type=int, default=1)
    ### output parameters
    parser.add_argument("--output", type=str, default="results/demo_bfr_aligned")
    ### common parameters
    parser.add_argument("--seed", type=int, default=231)
    parser.add_argument("--device", type=str, default="cpu", choices=["cpu", "cuda", "mps"])

    return parser.parse_args([])  # 先返回一个空的 Namespace 对象，然后再手动设置属性


def main_fr(params: dict):
    args = parse_args_from_dict(params)
    # 这里可以通过调整参数得到
    args.device = check_device(args.device)
    set_seed(args.seed)
    if args.version == "v1":
        V1InferenceLoop(args).run()
    else:
        supported_tasks = {
            "sr": BSRInferenceLoop,
            "dn": BIDInferenceLoop,
            "fr": BFRInferenceLoop,
            "fr_bg": UnAlignedBFRInferenceLoop
        }
        supported_tasks[args.task](args).run()
        print("done!")
