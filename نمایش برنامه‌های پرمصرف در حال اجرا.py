import psutil

def list_high_memory_processes(limit=10):
    processes = [(p.info['name'], p.info['memory_info'].rss)
                 for p in psutil.process_iter(['name', 'memory_info'])]
    processes.sort(key=lambda x: x[1], reverse=True)

    print(f"Top {limit} memory-consuming processes:")
    for name, memory in processes[:limit]:
        print(f"{name}: {memory / (1024 ** 2):.2f} MB")

def kill_process(pid):
    try:
        p = psutil.Process(pid)
        p.terminate()
        p.wait(timeout=3)
        print(f"Process {pid} terminated.")
    except Exception as e:
        print(f"Error terminating process {pid}: {e}")

list_high_memory_processes()
# To kill a specific process, you can use:
# kill_process(<PID>)
