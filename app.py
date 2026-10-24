tasks = []

def add_task(task_name):
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")

if __name__ == "__main__":
    print("Ứng dụng Quản lý công việc đã sẵn sàng!")
    add_task("Học Git và GitHub")