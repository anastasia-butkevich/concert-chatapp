import threading
from .utils.run_utils import run_fastapi, run_streamlit


if __name__ == "__main__":
    api_thread = threading.Thread(target=run_fastapi)
    api_thread.start()

    run_streamlit()
