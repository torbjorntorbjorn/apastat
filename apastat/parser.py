from apastat.model import Status


def parse(document):
    # Isolate stats list
    ends_on_stat_list = document.split("</dl>")[1]
    stat_list = ends_on_stat_list.split("\n")[1:-1]

    # Clean away markup tags
    stat_list = [x[4:] for x in stat_list]
    stat_list = [x[:-5] for x in stat_list]

    # Options for Status object
    options = {}

    for stat in stat_list:
        if "requests/sec" in stat:
            # Not sure what to do with this line,
            # some data points do not seeem very useful
            continue

        if "CPU Usage:" in stat:
            # Not sure what this line means, skipping for now
            continue

        # This line has a different format, but the data is good
        if "requests currently being processed" in stat:
            stat_split = stat.split(" ")
            options["requests_being_processed"] = stat_split[0]
            options["idle_workers"] = stat_split[5]
            continue

        # "Generic" parsing
        name, value = stat.split(":", 1)

        # Special case, this line has two data points in it
        if name == "Total accesses":
            # Variables "name" and "value" get handled as usual
            value, total_traffic = [x.strip() for x in value.split("-")]

            # "total_traffic" is a special case, handled here
            options["total_traffic"] = total_traffic.split(":")[1].strip()

        name = name.replace(" ", "_").lower()
        options[name] = value.strip()

    # Grab only the table of workers
    starts_on_table = document.split('<table border="0">')[1]
    only_table = starts_on_table.split("</table>")[0]

    # Split on </tr>, so that we end up with lines
    rows = only_table.split("</tr>")[1:]
    rows = [r.strip().replace("<tr>", "") for r in rows]
    rows = [r for r in rows if r]  # Some elements might have ended up as ""

    # Will be the return value
    status = Status(**options)

    for row in rows:
        # Holds cleaned column values
        cols = []

        # Clean each column
        for c in row.split("</td>"):
            c = c.replace("<td>", "").strip()
            c = c.replace("<td nowrap>", "").strip()
            c = c.replace("<b>", "").replace("</b>", "")

            # Some columns might have ended up as "", let's skip those
            if c:
                cols.append(c)

        # Add worker to status object
        status.add_worker(cols)

    return status
