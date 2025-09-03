import sys
import subprocess

WORKLOADS = {
    "llm": "python -m vllm.entrypoints.api_server --model path/or/name",
    "vision": "python -m my_vision_server",
}

def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Usage: launch_workload.py [workload]")
    workload = sys.argv[1]
    cmd = WORKLOADS.get(workload)
    if cmd is None:
        raise SystemExit(f"Unknown workload: {workload}")
    subprocess.run(cmd, shell=True, check=True)

if __name__ == "__main__":
    main()
