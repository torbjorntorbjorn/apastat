import apastat.io
import apastat.parser


def run(url, all_workers=False, order_by=""):
    document = apastat.io.get_document(url)
    status = apastat.parser.parse(document)

    # Work with all workers, or just the active ones ?
    if all_workers:
        workers = status.all_workers
    else:
        workers = status.active_workers

    # Prepare the static fields
    frmt = "% -8s % -6s % -5s % -4s % -16s"

    # Figure out max vhost lenght, add field to format string
    longest_vhost = max([len(w.vhost) for w in workers])
    frmt += " %% -%ss" % (longest_vhost)

    # Add a free-length field last for request
    frmt += " %s"

    print frmt % ("Srv", "PID", "Mode", "SS", "Client", "Vhost", "Request")

    if order_by == "seconds_since":
        iter_workers = sorted(workers, key=lambda w: w.seconds_since, reverse=True)
    elif order_by == "client":
        iter_workers = sorted(workers, key=lambda w: w.client, reverse=True)
    else:
        iter_workers = workers

    for worker in iter_workers:
        print frmt % (worker.srv, worker.pid, worker.mode,
            worker.seconds_since, worker.client, worker.vhost, worker.request)


scoreboard_key = """
Scoreboard key for Apache mod_status.

_ : Waiting for Connection
S : Starting up
R : Reading Request
W : Sending Reply
K : Keepalive (read)
D : DNS Lookup
C : Closing connection
L : Logging
G : Gracefully finishing
I : Idle cleanup of worker
. : Open slot with no current process
""".strip()
