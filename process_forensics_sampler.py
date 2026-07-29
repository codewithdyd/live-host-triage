import psutil
import random


class ProcessInfo:

    def process_info(self):
        print('Printing all the PIDs:')
        print(psutil.pids())
        pid = random.choice(psutil.pids())
        print('\nPrinting details about a randomly selected process: ')
        print('Process ID (PID): ', pid)
        process = psutil.Process(pid)
        print('\n===== Process basic details =====')
        print('\n--- Process name: ', process.name())
        print('\n--- Process status: ', process.status())
        print('\n--- Process username (started as): ', process.username())
        print('\n--- Process created at: ', process.create_time())
        print('\n--- Process executable: ', process.exe())
        print('\n--- Process working directory: ', process.cwd())
        print('\n--- Process command line: ', process.cmdline())
        print('\n--- Process children: ', process.children(recursive=True))
        print('\n--- Process parent: ', process.parent)
        print('\n===== Process memory and CPU information =====')
        print('\n--- Process CPU percent: ', process.cpu_percent())
        print('\n--- Process CPU times (accumulated CPU time): ', process.
        cpu_times())
        print('\n--- Process memory percent: ', process.memory_percent())
        print('\n--- Process memory info: ', process.memory_info())

        # printing network connection of a specif process
        connections = process.net_connections(kind = 'inet')
        print("\n--- Process connections:")

        if connections:
            for c in connections:
                laddr = f"{c.laddr.ip}:{c.laddr.port}" if c.laddr else "N/A"
                raddr = f"{c.raddr.ip}:{c.raddr.port}" if c.raddr else "*:*"
                print(f"  [{c.status:<11}] Source: {laddr:<21} -> Dest: {raddr}")
        else:
            print("  None")
       
    

if __name__ == "__main__":
    infot = ProcessInfo()
    infot.process_info()
