class Status(object):
    '''Represents the output from Apache mod-status module'''

    def __init__(self, **options):
        # Will hold Worker objects
        self._workers = []

        # The stats data from the top of the mod-status document
        self._current_time = (options["current_time"]
            if "current_time" in options else "")

        self._restart_time = (options["restart_time"]
            if "restart_time" in options else "")

        self._parent_server_generation = (options["parent_server_generation"]
            if "parent_server_generation" in options else "")

        self._server_uptime = (options["server_uptime"]
            if "server_uptime" in options else "")

        self._total_accesses = (options["total_accesses"]
            if "total_accesses" in options else "")

        self._requests_being_processed = (options["requests_being_processed"]
            if "requests_being_processed" in options else "")

        self._idle_workers = (options["idle_workers"]
            if "idle_workers" in options else "")

    @property
    def current_time(self):
        return self._current_time

    @property
    def restart_time(self):
        return self._restart_time

    @property
    def parent_server_generation(self):
        return self._parent_server_generation

    @property
    def server_uptime(self):
        return self._server_uptime

    @property
    def total_accesses(self):
        return self._total_accesses

    @property
    def requests_being_processed(self):
        return self._requests_being_processed

    @property
    def idle_workers(self):
        return self._idle_workers

    @property
    def active_workers(self):
        return [w for w in self.workers if w.is_active()]

    @property
    def workers(self):
        return self._workers

    @property
    def all_workers(self):
        return self.workers

    def add_worker(self, data):
        self.workers.append(Worker(data))


class Worker(object):
    def __init__(self, data):
        # These names are re-used from the mod_status source
        self._id, self._generation = data[0].split("-")
        self._pid = data[1]
        conn_lres, my_lres, lres = data[2].split("/")
        self._status = data[3]
        self._cpu = data[4]
        self._ss = int(data[5])
        self._req = data[6]
        self._conn = data[7]
        self._child = data[8]
        self._slot = data[9]
        self._client = data[10]
        self._vhost = data[11]
        self._request = data[12]

    def is_active(self):
        # We consider all modes except "idle" and "empty slot" to be active
        return self._status not in ["_", "."]

    @property
    def pid(self):
        return self._pid

    @property
    def srv(self):
        return "-".join([self._id, self._generation])

    @property
    def mode(self):
        return self._status

    @property
    def client(self):
        return self._client

    @property
    def vhost(self):
        return self._vhost

    @property
    def request(self):
        return self._request

    @property
    def seconds_since(self):
        return self._ss
