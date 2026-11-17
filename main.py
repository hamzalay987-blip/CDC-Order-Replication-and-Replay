import json
from pathlib import Path

def apply(events, state=None):
    state={} if state is None else state
    for e in events:
        key=e['order_id']; prior=state.get(key)
        if prior and e['sequence']<=prior['sequence']: continue
        state[key]={'sequence':e['sequence'],'amount':None if e['op']=='delete' else e.get('amount')}
    return state

def run(path='data/changes.jsonl'):
    events=[json.loads(x) for x in Path(path).read_text().splitlines() if x.strip()]
    state=apply(events)
    state=apply(events,state)  # replay is intentional
    live={k:v['amount'] for k,v in state.items() if v['amount'] is not None}
    return {'events_seen':len(events),'live_orders':live,'last_sequences':{k:v['sequence'] for k,v in state.items()}}

if __name__ == '__main__':
    import json
    print(json.dumps(run(), indent=2))
