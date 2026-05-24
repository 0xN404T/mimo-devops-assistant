import os, subprocess, httpx, typer
from rich import print
from dotenv import load_dotenv
load_dotenv(); app=typer.Typer()

def run(cmd): return subprocess.run(cmd,shell=True,text=True,capture_output=True,timeout=20).stdout[-4000:]
def ask(ctx):
    prompt='Analyze this Linux server diagnostic output. Give safe actionable fixes only.\n\n'+ctx
    r=httpx.post(os.getenv('MIMO_URL','https://platform.xiaomimimo.com/v1/chat/completions'),headers={'Authorization':f"Bearer {os.getenv('MIMO_API_KEY','')}"},json={'model':os.getenv('MIMO_MODEL','mimo-v2.5'),'messages':[{'role':'user','content':prompt}]},timeout=120)
    data=r.json(); return data.get('choices',[{}])[0].get('message',{}).get('content',str(data))

@app.command()
def diagnose():
    ctx='## df\n'+run('df -h')+'\n## memory\n'+run('free -h')+'\n## top processes\n'+run('ps aux --sort=-%mem | head -15')
    print(ask(ctx))

if __name__=='__main__': app()
