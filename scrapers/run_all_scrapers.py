import subprocess
import sys

scripts = ['scraper_botmaal.py', 'scraper_zmasti.py', 'scraper_mxseries.py', 'scraper_vmaal.py', 'scraper_mastiwala.py', 'scraper_redmaal.py', 'scraper_xmazaa.py', 'scraper_uncutmaza.py', 'scraper_xmaasti.py', 'scraper_webseriess.py', 'scraper_mxporn.py', 'scraper_uffmaal.py', 'scraper_zmaal.py', 'scraper_hotullu.py', 'scraper_playmaal.py', 'scraper_ymaal.py', 'scraper_aagmaal3.py', 'scraper_webxseries.py', 'scraper_opmaal.py']

for script in scripts:
    print(f"\n===========================")
    print(f"Running {script}")
    print(f"===========================\n")
    # Using sys.executable to ensure we use the same Python environment
    subprocess.run([sys.executable, script])

print("\nAll scrapers finished!")
