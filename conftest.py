import os

from leapp.repository.scan import scan_repo


def pytest_sessionstart(session):
    actor_path = os.environ['LEAPP_TESTED_ACTOR']
    repo = scan_repo(('/'.join(actor_path.split('/')[:-2])))
    actor = None
    for a in repo.actors:
        if a.full_path == actor_path:
            actor = a
            break

    if not actor:
        return

    session.actor_context = actor.injected_context()
    session.actor_context.__enter__()