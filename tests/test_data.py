# flake8: noqa

document_single_worker = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html><head>
<title>Apache Status</title>
</head><body>
<h1>Apache Server Status for localhost</h1>

<dl><dt>Server Version: Apache/2.2.16 (Debian) PHP/5.3.3-7+squeeze8 with Suhosin-Patch mod_wsgi/3.3 Python/2.6.6</dt>
<dt>Server Built: Apr  1 2012 07:14:38
</dt></dl><hr /><dl>
<dt>Current Time: Thursday, 14-Jun-2012 22:36:43 CEST</dt>
<dt>Restart Time: Monday, 16-Apr-2012 10:49:27 CEST</dt>
<dt>Parent Server Generation: 22</dt>
<dt>Server uptime:  59 days 11 hours 47 minutes 15 seconds</dt>
<dt>Total accesses: 3266 - Total Traffic: 10.7 MB</dt>
<dt>CPU Usage: u.35 s.15 cu0 cs0 - 9.73e-6% CPU load</dt>
<dt>.000635 requests/sec - 2 B/second - 3425 B/request</dt>
<dt>1 requests currently being processed, 7 idle workers</dt>
</dl><pre>____._._._W.....................................................
................................................................
................................................................
................................................................
</pre>
<p>Scoreboard Key:<br />
"<b><code>_</code></b>" Waiting for Connection, 
"<b><code>S</code></b>" Starting up, 
"<b><code>R</code></b>" Reading Request,<br />
"<b><code>W</code></b>" Sending Reply, 
"<b><code>K</code></b>" Keepalive (read), 
"<b><code>D</code></b>" DNS Lookup,<br />
"<b><code>C</code></b>" Closing connection, 
"<b><code>L</code></b>" Logging, 
"<b><code>G</code></b>" Gracefully finishing,<br /> 
"<b><code>I</code></b>" Idle cleanup of worker, 
"<b><code>.</code></b>" Open slot with no current process</p>
<p />


<table border="0"><tr><th>Srv</th><th>PID</th><th>Acc</th><th>M</th><th>CPU
</th><th>SS</th><th>Req</th><th>Conn</th><th>Child</th><th>Slot</th><th>Client</th><th>VHost</th><th>Request</th></tr>

<tr><td><b>0-22</b></td><td>3968</td><td>0/11/350</td><td>_
</td><td>0.01</td><td>16723</td><td>0</td><td>0.0</td><td>0.01</td><td>0.40
</td><td>193.91.180.234</td><td nowrap>dashboard.example.net</td><td nowrap>GET /gntstats/scripts/backbone-min.js HTTP/1.1</td></tr>

<tr><td><b>1-22</b></td><td>3963</td><td>0/8/379</td><td>_
</td><td>0.01</td><td>16898</td><td>0</td><td>0.0</td><td>0.00</td><td>0.61
</td><td>193.91.180.234</td><td nowrap>dashboard.example.net</td><td nowrap>GET /favicon.ico HTTP/1.1</td></tr>

<tr><td><b>2-22</b></td><td>3969</td><td>0/1/284</td><td>_
</td><td>0.00</td><td>16712</td><td>0</td><td>0.0</td><td>0.00</td><td>0.55
</td><td>193.91.180.234</td><td nowrap>dashboard.example.net</td><td nowrap>GET /gntstats/scripts/app.js HTTP/1.1</td></tr>

<tr><td><b>3-22</b></td><td>4067</td><td>0/1/169</td><td>_
</td><td>0.00</td><td>16899</td><td>0</td><td>0.0</td><td>0.00</td><td>0.05
</td><td>193.91.180.234</td><td nowrap>dashboard.example.net</td><td nowrap>GET /gntstats/scripts/backbone-min.js HTTP/1.1</td></tr>

<tr><td><b>4-21</b></td><td>-</td><td>0/0/202</td><td>.
</td><td>0.00</td><td>17591</td><td>0</td><td>0.0</td><td>0.00</td><td>3.20
</td><td>::1</td><td nowrap>torbjorn-dev.example.net</td><td nowrap>OPTIONS * HTTP/1.0</td></tr>

<tr><td><b>5-22</b></td><td>3964</td><td>0/11/229</td><td>_
</td><td>0.02</td><td>16705</td><td>0</td><td>0.0</td><td>0.00</td><td>3.44
</td><td>193.91.180.234</td><td nowrap>dashboard.example.net</td><td nowrap>GET /favicon.ico HTTP/1.1</td></tr>

<tr><td><b>6-16</b></td><td>-</td><td>0/0/314</td><td>.
</td><td>0.01</td><td>402516</td><td>0</td><td>0.0</td><td>0.00</td><td>0.43
</td><td>::1</td><td nowrap>torbjorn-dev.example.net</td><td nowrap>OPTIONS * HTTP/1.0</td></tr>

<tr><td><b>7-22</b></td><td>3965</td><td>0/14/188</td><td>_
</td><td>0.02</td><td>10097</td><td>12</td><td>0.0</td><td>0.00</td><td>0.12
</td><td>202.157.182.15</td><td nowrap>torbjorn-dev.example.net</td><td nowrap>GET / HTTP/1.1</td></tr>

<tr><td><b>8-16</b></td><td>-</td><td>0/0/345</td><td>.
</td><td>0.00</td><td>402516</td><td>0</td><td>0.0</td><td>0.00</td><td>0.46
</td><td>::1</td><td nowrap>torbjorn-dev.example.net</td><td nowrap>OPTIONS * HTTP/1.0</td></tr>

<tr><td><b>9-22</b></td><td>3966</td><td>0/6/369</td><td>_
</td><td>0.01</td><td>16723</td><td>0</td><td>0.0</td><td>0.00</td><td>0.52
</td><td>193.91.180.234</td><td nowrap>dashboard.example.net</td><td nowrap>GET /gntstats/scripts/app.js HTTP/1.1</td></tr>

<tr><td><b>10-22</b></td><td>3967</td><td>0/1/114</td><td><b>W</b>
</td><td>0.00</td><td>0</td><td>0</td><td>0.0</td><td>0.01</td><td>0.35
</td><td>::1</td><td nowrap>torbjorn-dev.example.net</td><td nowrap>GET /server-status HTTP/1.1</td></tr>

<tr><td><b>11-13</b></td><td>-</td><td>0/0/301</td><td>.
</td><td>0.41</td><td>1612980</td><td>0</td><td>0.0</td><td>0.00</td><td>0.53
</td><td>::1</td><td nowrap>torbjorn-dev.example.net</td><td nowrap>OPTIONS * HTTP/1.0</td></tr>

<tr><td><b>12-15</b></td><td>-</td><td>0/0/13</td><td>.
</td><td>0.01</td><td>834570</td><td>0</td><td>0.0</td><td>0.00</td><td>0.00
</td><td>::1</td><td nowrap>torbjorn-dev.example.net</td><td nowrap>OPTIONS * HTTP/1.0</td></tr>

<tr><td><b>13-15</b></td><td>-</td><td>0/0/9</td><td>.
</td><td>0.00</td><td>834570</td><td>0</td><td>0.0</td><td>0.00</td><td>0.00
</td><td>::1</td><td nowrap>torbjorn-dev.example.net</td><td nowrap>OPTIONS * HTTP/1.0</td></tr>

</table>
 <hr /> <table>
 <tr><th>Srv</th><td>Child Server number - generation</td></tr>
 <tr><th>PID</th><td>OS process ID</td></tr>
 <tr><th>Acc</th><td>Number of accesses this connection / this child / this slot</td></tr>
 <tr><th>M</th><td>Mode of operation</td></tr>
<tr><th>CPU</th><td>CPU usage, number of seconds</td></tr>
<tr><th>SS</th><td>Seconds since beginning of most recent request</td></tr>
 <tr><th>Req</th><td>Milliseconds required to process most recent request</td></tr>
 <tr><th>Conn</th><td>Kilobytes transferred this connection</td></tr>
 <tr><th>Child</th><td>Megabytes transferred this child</td></tr>
 <tr><th>Slot</th><td>Total megabytes transferred this slot</td></tr>
 </table>
<hr />
<address>Apache/2.2.16 (Debian) Server at localhost Port 80</address>
</body></html>"""

document_multiple_workers = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html><head>
<title>Apache Status</title>
</head><body>
<h1>Apache Server Status for www.example.net</h1>

<dl><dt>Server Version: Apache/2.2.20 (Unix) mod_ssl/2.2.20 OpenSSL/0.9.8g DAV/2 PHP/5.2.17</dt>
<dt>Server Built: Sep  6 2011 20:31:21
</dt></dl><hr /><dl>
<dt>Current Time: Thursday, 14-Jun-2012 22:51:49 CEST</dt>
<dt>Restart Time: Thursday, 14-Jun-2012 00:30:06 CEST</dt>
<dt>Parent Server Generation: 0</dt>
<dt>Server uptime:  22 hours 21 minutes 43 seconds</dt>
<dt>Total accesses: 209013 - Total Traffic: 1.6 GB</dt>
<dt>CPU Usage: u133.43 s92.48 cu0 cs0 - .281% CPU load</dt>
<dt>2.6 requests/sec - 21.3 kB/second - 8.2 kB/request</dt>
<dt>8 requests currently being processed, 13 idle workers</dt>
</dl><pre>W_.KK._W..R_.C___.WW__..___._._.................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
..</pre>
<p>Scoreboard Key:<br />
"<b><code>_</code></b>" Waiting for Connection, 
"<b><code>S</code></b>" Starting up, 
"<b><code>R</code></b>" Reading Request,<br />
"<b><code>W</code></b>" Sending Reply, 
"<b><code>K</code></b>" Keepalive (read), 
"<b><code>D</code></b>" DNS Lookup,<br />
"<b><code>C</code></b>" Closing connection, 
"<b><code>L</code></b>" Logging, 
"<b><code>G</code></b>" Gracefully finishing,<br /> 
"<b><code>I</code></b>" Idle cleanup of worker, 
"<b><code>.</code></b>" Open slot with no current process</p>
<p />


<table border="0"><tr><th>Srv</th><th>PID</th><th>Acc</th><th>M</th><th>CPU
</th><th>SS</th><th>Req</th><th>Conn</th><th>Child</th><th>Slot</th><th>Client</th><th>VHost</th><th>Request</th></tr>

<tr><td><b>0-0</b></td><td>14426</td><td>0/8/14107</td><td><b>W</b>
</td><td>0.00</td><td>0</td><td>0</td><td>0.0</td><td>0.41</td><td>106.78
</td><td>66.249.66.102</td><td nowrap>vhost1.example.net</td><td nowrap>GET /catalogsearch/result/index/?cat=3&amp;limit=50&amp;mode=list&amp;q=bjj</td></tr>

<tr><td><b>1-0</b></td><td>14324</td><td>0/31/14353</td><td>_
</td><td>9.09</td><td>4</td><td>611</td><td>0.0</td><td>0.19</td><td>111.89
</td><td>66.249.66.87</td><td nowrap>vhost2.example.net</td><td nowrap>GET /sykler-1.html?cat=62&amp;dir=desc&amp;limit=10&amp;manufacturer=20&amp;mat</td></tr>

<tr><td><b>2-0</b></td><td>-</td><td>0/0/13769</td><td>.
</td><td>0.58</td><td>2</td><td>0</td><td>0.0</td><td>0.00</td><td>108.54
</td><td>88.89.21.63</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>3-0</b></td><td>14443</td><td>1/3/13666</td><td><b>K</b>
</td><td>0.00</td><td>0</td><td>6954</td><td>142.4</td><td>0.15</td><td>112.77
</td><td>88.89.21.63</td><td nowrap>vhost3.example.net</td><td nowrap>GET /media//50-smaker_960x350_WEB.jpg HTTP/1.1</td></tr>

<tr><td><b>4-0</b></td><td>13971</td><td>1/96/13732</td><td><b>K</b>
</td><td>17.05</td><td>0</td><td>7156</td><td>154.7</td><td>0.34</td><td>109.55
</td><td>88.89.21.63</td><td nowrap>vhost3.example.net</td><td nowrap>GET /skin/frontend/melba/default/img/backgrounds/melba_backgrou</td></tr>

<tr><td><b>5-0</b></td><td>-</td><td>0/0/12939</td><td>.
</td><td>3.44</td><td>0</td><td>1444</td><td>0.0</td><td>0.00</td><td>102.85
</td><td>66.249.71.242</td><td nowrap>vhost4.example.net</td><td nowrap>GET /enable-cookies HTTP/1.1</td></tr>

<tr><td><b>6-0</b></td><td>14446</td><td>0/8/12461</td><td>_
</td><td>0.00</td><td>3</td><td>0</td><td>0.0</td><td>0.01</td><td>106.94
</td><td>88.89.21.63</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>7-0</b></td><td>14043</td><td>0/94/12218</td><td><b>W</b>
</td><td>9.91</td><td>7</td><td>0</td><td>0.0</td><td>3.91</td><td>104.37
</td><td>88.89.21.63</td><td nowrap>vhost3.example.net</td><td nowrap>GET /media//LOVE.jpg HTTP/1.1</td></tr>

<tr><td><b>8-0</b></td><td>-</td><td>0/0/11510</td><td>.
</td><td>1.02</td><td>3</td><td>0</td><td>0.0</td><td>0.00</td><td>82.43
</td><td>88.89.21.63</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>9-0</b></td><td>-</td><td>0/0/11186</td><td>.
</td><td>6.76</td><td>1</td><td>0</td><td>0.0</td><td>0.00</td><td>83.62
</td><td>89.20.241.163</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>10-0</b></td><td>14163</td><td>0/40/10076</td><td><b>R</b>
</td><td>6.82</td><td>47</td><td>0</td><td>0.0</td><td>0.16</td><td>77.19
</td><td>?</td><td nowrap>?</td><td nowrap>..reading.. </td></tr>

<tr><td><b>11-0</b></td><td>14164</td><td>0/55/10774</td><td>_
</td><td>5.52</td><td>3</td><td>0</td><td>0.0</td><td>0.41</td><td>96.64
</td><td>85.167.160.190</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>12-0</b></td><td>-</td><td>0/0/8647</td><td>.
</td><td>4.98</td><td>6</td><td>0</td><td>0.0</td><td>0.00</td><td>75.83
</td><td>84.211.127.2</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>13-0</b></td><td>14174</td><td>0/25/8040</td><td><b>C</b>
</td><td>17.03</td><td>0</td><td>0</td><td>0.0</td><td>0.04</td><td>63.14
</td><td>88.89.21.63</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>14-0</b></td><td>14362</td><td>0/46/6497</td><td>_
</td><td>4.20</td><td>3</td><td>0</td><td>0.0</td><td>0.37</td><td>53.65
</td><td>85.167.160.190</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>15-0</b></td><td>14436</td><td>0/31/6406</td><td>_
</td><td>1.22</td><td>0</td><td>0</td><td>0.0</td><td>0.22</td><td>52.66
</td><td>85.167.160.190</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>16-0</b></td><td>14437</td><td>0/15/5196</td><td>_
</td><td>0.02</td><td>3</td><td>0</td><td>0.0</td><td>0.18</td><td>40.97
</td><td>85.167.160.190</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>17-0</b></td><td>-</td><td>0/0/4045</td><td>.
</td><td>2.31</td><td>4</td><td>0</td><td>0.0</td><td>0.00</td><td>30.81
</td><td>81.175.47.93</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>18-0</b></td><td>14447</td><td>0/5/2597</td><td><b>W</b>
</td><td>0.00</td><td>0</td><td>0</td><td>0.0</td><td>0.02</td><td>18.91
</td><td>109.247.69.193</td><td nowrap>localhost</td><td nowrap>GET /server-status HTTP/1.1</td></tr>

<tr><td><b>19-0</b></td><td>14448</td><td>0/4/2744</td><td><b>W</b>
</td><td>0.00</td><td>5</td><td>0</td><td>0.0</td><td>0.01</td><td>20.03
</td><td>88.89.21.63</td><td nowrap>vhost3.example.net</td><td nowrap>GET /media//COFFIE.jpg HTTP/1.1</td></tr>

<tr><td><b>20-0</b></td><td>14449</td><td>0/9/1934</td><td>_
</td><td>0.88</td><td>3</td><td>0</td><td>0.0</td><td>0.18</td><td>16.68
</td><td>85.167.160.190</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>21-0</b></td><td>14450</td><td>0/8/1568</td><td>_
</td><td>0.00</td><td>3</td><td>0</td><td>0.0</td><td>0.16</td><td>13.80
</td><td>85.167.160.190</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>22-0</b></td><td>-</td><td>0/0/1628</td><td>.
</td><td>0.00</td><td>5</td><td>4</td><td>0.0</td><td>0.00</td><td>11.35
</td><td>89.20.241.163</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>23-0</b></td><td>-</td><td>0/0/1893</td><td>.
</td><td>2.24</td><td>9</td><td>0</td><td>0.0</td><td>0.00</td><td>13.14
</td><td>84.212.66.35</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>24-0</b></td><td>14454</td><td>0/5/1796</td><td>_
</td><td>0.00</td><td>0</td><td>0</td><td>0.0</td><td>0.02</td><td>13.50
</td><td>88.89.21.63</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>25-0</b></td><td>14455</td><td>0/4/1152</td><td>_
</td><td>0.68</td><td>1</td><td>751</td><td>0.0</td><td>0.00</td><td>8.30
</td><td>66.249.71.249</td><td nowrap>vhost6.example.net</td><td nowrap>GET /loft-og-surring/lofteutstyr/flatstropper-bandstropper.html</td></tr>

<tr><td><b>26-0</b></td><td>14456</td><td>0/4/515</td><td>_
</td><td>0.00</td><td>0</td><td>0</td><td>0.0</td><td>0.01</td><td>2.57
</td><td>88.89.21.63</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>27-0</b></td><td>-</td><td>0/0/244</td><td>.
</td><td>0.00</td><td>8</td><td>1</td><td>0.0</td><td>0.00</td><td>1.16
</td><td>84.234.186.16</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>28-0</b></td><td>14458</td><td>0/3/191</td><td>_
</td><td>0.00</td><td>4</td><td>263</td><td>0.0</td><td>0.30</td><td>2.62
</td><td>81.175.47.93</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>29-0</b></td><td>-</td><td>0/0/183</td><td>.
</td><td>5.45</td><td>7</td><td>632</td><td>0.0</td><td>0.00</td><td>1.39
</td><td>66.249.66.228</td><td nowrap>vhost6.example.net</td><td nowrap>GET /batteri/mc-batteri.html?batteri_bredde=389&amp;batteri_hoyde=1</td></tr>

<tr><td><b>30-0</b></td><td>14460</td><td>0/2/217</td><td>_
</td><td>0.00</td><td>5</td><td>1</td><td>0.0</td><td>0.00</td><td>1.30
</td><td>109.247.69.193</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>31-0</b></td><td>-</td><td>0/0/92</td><td>.
</td><td>13.69</td><td>1433</td><td>0</td><td>0.0</td><td>0.00</td><td>0.55
</td><td>80.212.115.8</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>32-0</b></td><td>-</td><td>0/0/221</td><td>.
</td><td>4.06</td><td>1432</td><td>2184</td><td>0.0</td><td>0.00</td><td>1.93
</td><td>66.249.72.212</td><td nowrap>vhost5.example.net</td><td nowrap>GET /catalogsearch/result/index/?___from_store=default&amp;___store</td></tr>

<tr><td><b>33-0</b></td><td>-</td><td>0/0/166</td><td>.
</td><td>8.55</td><td>1316</td><td>3</td><td>0.0</td><td>0.00</td><td>1.80
</td><td>212.251.207.194</td><td nowrap>vhost12.example.net</td><td nowrap>GET /skin/frontend/silver/default/css/styles.css HTTP/1.1</td></tr>

<tr><td><b>34-0</b></td><td>-</td><td>0/0/296</td><td>.
</td><td>22.92</td><td>977</td><td>468</td><td>0.0</td><td>0.00</td><td>2.29
</td><td>66.249.66.123</td><td nowrap>vhost7.example.net</td><td nowrap>GET /page/6/ HTTP/1.1</td></tr>

<tr><td><b>35-0</b></td><td>-</td><td>0/0/72</td><td>.
</td><td>0.00</td><td>1419</td><td>0</td><td>0.0</td><td>0.00</td><td>0.31
</td><td>109.189.201.160</td><td nowrap>vhost8.example.net</td><td nowrap>GET /skin/frontend/silver/default/silverframework/highslide/gra</td></tr>

<tr><td><b>36-0</b></td><td>-</td><td>0/0/80</td><td>.
</td><td>0.01</td><td>1420</td><td>0</td><td>0.0</td><td>0.00</td><td>0.68
</td><td>109.189.201.160</td><td nowrap>vhost8.example.net</td><td nowrap>GET /media/footer/nets.gif HTTP/1.1</td></tr>

<tr><td><b>37-0</b></td><td>-</td><td>0/0/170</td><td>.
</td><td>0.00</td><td>1431</td><td>2</td><td>0.0</td><td>0.00</td><td>2.91
</td><td>66.160.159.108</td><td nowrap>vhost9.example.net</td><td nowrap>GET /index.php/feeds/rss HTTP/1.0</td></tr>

<tr><td><b>38-0</b></td><td>-</td><td>0/0/189</td><td>.
</td><td>0.00</td><td>1414</td><td>0</td><td>0.0</td><td>0.00</td><td>0.81
</td><td>84.234.170.46</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>39-0</b></td><td>-</td><td>0/0/311</td><td>.
</td><td>34.60</td><td>1430</td><td>2</td><td>0.0</td><td>0.00</td><td>2.25
</td><td>84.234.172.249</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>40-0</b></td><td>-</td><td>0/0/85</td><td>.
</td><td>3.30</td><td>1369</td><td>0</td><td>0.0</td><td>0.00</td><td>1.48
</td><td>84.208.76.7</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>41-0</b></td><td>-</td><td>0/0/107</td><td>.
</td><td>0.00</td><td>1405</td><td>0</td><td>0.0</td><td>0.00</td><td>0.69
</td><td>82.116.84.206</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>42-0</b></td><td>-</td><td>0/0/194</td><td>.
</td><td>0.64</td><td>1429</td><td>6294</td><td>0.0</td><td>0.00</td><td>1.79
</td><td>220.181.108.182</td><td nowrap>vhost10.example.net</td><td nowrap>GET / HTTP/1.1</td></tr>

<tr><td><b>43-0</b></td><td>-</td><td>0/0/224</td><td>.
</td><td>0.00</td><td>24941</td><td>1</td><td>0.0</td><td>0.00</td><td>1.97
</td><td>88.91.58.25</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>44-0</b></td><td>-</td><td>0/0/24</td><td>.
</td><td>0.00</td><td>34734</td><td>0</td><td>0.0</td><td>0.00</td><td>0.79
</td><td>84.202.53.170</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>45-0</b></td><td>-</td><td>0/0/45</td><td>.
</td><td>0.60</td><td>34711</td><td>723</td><td>0.0</td><td>0.00</td><td>0.18
</td><td>80.69.225.182</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>46-0</b></td><td>-</td><td>0/0/59</td><td>.
</td><td>0.00</td><td>34731</td><td>1</td><td>0.0</td><td>0.00</td><td>0.79
</td><td>84.202.53.170</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>47-0</b></td><td>-</td><td>0/0/9</td><td>.
</td><td>0.66</td><td>34701</td><td>4</td><td>0.0</td><td>0.00</td><td>0.05
</td><td>82.147.63.222</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>48-0</b></td><td>-</td><td>0/0/29</td><td>.
</td><td>2.85</td><td>34648</td><td>8</td><td>0.0</td><td>0.00</td><td>0.28
</td><td>2.149.182.84</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>49-0</b></td><td>-</td><td>0/0/2</td><td>.
</td><td>0.00</td><td>34730</td><td>1</td><td>0.0</td><td>0.00</td><td>0.01
</td><td>84.202.53.170</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>50-0</b></td><td>-</td><td>0/0/26</td><td>.
</td><td>0.08</td><td>34656</td><td>99</td><td>0.0</td><td>0.00</td><td>0.07
</td><td>109.247.69.200</td><td nowrap>vhost12.example.net</td><td nowrap>GET /sendsms/cron/sendMessageQueue HTTP/1.1</td></tr>

<tr><td><b>51-0</b></td><td>-</td><td>0/0/175</td><td>.
</td><td>7.23</td><td>34576</td><td>0</td><td>0.0</td><td>0.00</td><td>2.22
</td><td>82.147.63.222</td><td nowrap>vhost12.example.net</td><td nowrap>GET /skin/frontend/base/default/css/silver-black.css HTTP/1.1</td></tr>

<tr><td><b>52-0</b></td><td>-</td><td>0/0/2</td><td>.
</td><td>0.00</td><td>34729</td><td>1</td><td>0.0</td><td>0.00</td><td>0.01
</td><td>84.202.53.170</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>53-0</b></td><td>-</td><td>0/0/2</td><td>.
</td><td>0.00</td><td>34728</td><td>1</td><td>0.0</td><td>0.00</td><td>0.01
</td><td>84.202.53.170</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>54-0</b></td><td>-</td><td>0/0/3</td><td>.
</td><td>0.08</td><td>34703</td><td>85</td><td>0.0</td><td>0.00</td><td>0.01
</td><td>109.247.69.200</td><td nowrap>vhost12.example.net</td><td nowrap>GET /sendsms/cron/pending HTTP/1.1</td></tr>

<tr><td><b>55-0</b></td><td>-</td><td>0/0/21</td><td>.
</td><td>0.76</td><td>34682</td><td>0</td><td>0.0</td><td>0.00</td><td>0.06
</td><td>2.149.182.84</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>56-0</b></td><td>-</td><td>0/0/2</td><td>.
</td><td>0.00</td><td>34727</td><td>0</td><td>0.0</td><td>0.00</td><td>0.00
</td><td>84.202.53.170</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>57-0</b></td><td>-</td><td>0/0/9</td><td>.
</td><td>0.12</td><td>34691</td><td>0</td><td>0.0</td><td>0.00</td><td>0.05
</td><td>188.149.29.127</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>58-0</b></td><td>-</td><td>0/0/2</td><td>.
</td><td>0.00</td><td>34720</td><td>1818</td><td>0.0</td><td>0.00</td><td>0.60
</td><td>84.202.53.170</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>59-0</b></td><td>-</td><td>0/0/2</td><td>.
</td><td>0.00</td><td>34726</td><td>0</td><td>0.0</td><td>0.00</td><td>0.01
</td><td>84.202.53.170</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>60-0</b></td><td>-</td><td>0/0/2</td><td>.
</td><td>0.00</td><td>34725</td><td>0</td><td>0.0</td><td>0.00</td><td>0.01
</td><td>84.202.53.170</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>61-0</b></td><td>-</td><td>0/0/48</td><td>.
</td><td>12.36</td><td>34497</td><td>2</td><td>0.0</td><td>0.00</td><td>0.12
</td><td>84.202.53.170</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>62-0</b></td><td>-</td><td>0/0/2</td><td>.
</td><td>0.00</td><td>34724</td><td>0</td><td>0.0</td><td>0.00</td><td>0.00
</td><td>84.202.53.170</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>63-0</b></td><td>-</td><td>0/0/2</td><td>.
</td><td>0.00</td><td>34723</td><td>0</td><td>0.0</td><td>0.00</td><td>0.00
</td><td>84.202.53.170</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>64-0</b></td><td>-</td><td>0/0/2</td><td>.
</td><td>0.00</td><td>34700</td><td>0</td><td>0.0</td><td>0.00</td><td>0.01
</td><td>84.202.53.170</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>65-0</b></td><td>-</td><td>0/0/4</td><td>.
</td><td>0.59</td><td>34707</td><td>392</td><td>0.0</td><td>0.00</td><td>0.12
</td><td>85.19.183.236</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>67-0</b></td><td>-</td><td>0/0/1</td><td>.
</td><td>0.54</td><td>34745</td><td>668</td><td>0.0</td><td>0.00</td><td>0.00
</td><td>66.249.66.198</td><td nowrap>vhost10.example.net</td><td nowrap>GET /stempel-4150-ts50x.html HTTP/1.1</td></tr>

<tr><td><b>69-0</b></td><td>-</td><td>0/0/10</td><td>.
</td><td>0.56</td><td>34686</td><td>0</td><td>0.0</td><td>0.00</td><td>0.04
</td><td>188.149.29.127</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>70-0</b></td><td>-</td><td>0/0/2</td><td>.
</td><td>0.58</td><td>34721</td><td>630</td><td>0.0</td><td>0.00</td><td>0.00
</td><td>80.69.225.182</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>72-0</b></td><td>-</td><td>0/0/4</td><td>.
</td><td>3.00</td><td>34699</td><td>2634</td><td>0.0</td><td>0.00</td><td>0.00
</td><td>66.249.72.171</td><td nowrap>vhost11.example.net</td><td nowrap>GET /electronics/computers/processors.html?___from_store=defaul</td></tr>

<tr><td><b>74-0</b></td><td>-</td><td>0/0/4</td><td>.
</td><td>2.98</td><td>34689</td><td>0</td><td>0.0</td><td>0.00</td><td>0.02
</td><td>188.149.29.127</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>75-0</b></td><td>-</td><td>0/0/2</td><td>.
</td><td>0.61</td><td>34718</td><td>704</td><td>0.0</td><td>0.00</td><td>0.00
</td><td>80.69.225.182</td><td nowrap>localhost</td><td nowrap>NULL</td></tr>

<tr><td><b>76-0</b></td><td>-</td><td>0/0/27</td><td>.
</td><td>5.36</td><td>34599</td><td>192</td><td>0.0</td><td>0.00</td><td>0.48
</td><td>109.247.69.200</td><td nowrap>vhost12.example.net</td><td nowrap>GET /sendsms/cron/sendMessageQueue HTTP/1.1</td></tr>

</table>
 <hr /> <table>
 <tr><th>Srv</th><td>Child Server number - generation</td></tr>
 <tr><th>PID</th><td>OS process ID</td></tr>
 <tr><th>Acc</th><td>Number of accesses this connection / this child / this slot</td></tr>
 <tr><th>M</th><td>Mode of operation</td></tr>
<tr><th>CPU</th><td>CPU usage, number of seconds</td></tr>
<tr><th>SS</th><td>Seconds since beginning of most recent request</td></tr>
 <tr><th>Req</th><td>Milliseconds required to process most recent request</td></tr>
 <tr><th>Conn</th><td>Kilobytes transferred this connection</td></tr>
 <tr><th>Child</th><td>Megabytes transferred this child</td></tr>
 <tr><th>Slot</th><td>Total megabytes transferred this slot</td></tr>
 </table>
<hr>
<table cellspacing=0 cellpadding=0>
<tr><td bgcolor="#000000">
<b><font color="#ffffff" face="Arial,Helvetica">SSL/TLS Session Cache Status:</font></b></td></tr>
<tr><td bgcolor="#ffffff">
cache type: <b>SHMCB</b>, shared memory: <b>512000</b> bytes, current sessions: <b>1</b><br>subcaches: <b>32</b>, indexes per subcache: <b>133</b><br>time left on oldest entries' SSL sessions: avg: <b>219</b> seconds, (range: 219...219)<br>index usage: <b>0%</b>, cache usage: <b>0%</b><br>total sessions stored since starting: <b>39</b><br>total sessions expired since starting: <b>38</b><br>total (pre-expiry) sessions scrolled out of the cache: <b>0</b><br>total retrieves since starting: <b>0</b> hit, <b>0</b> miss<br>total removes since starting: <b>0</b> hit, <b>0</b> miss<br></td></tr>
</table>
<hr />
<address>Apache/2 Server at www.example.net Port 80</address>
</body></html>
"""


if __name__ == "__main__":
    print document_multiple_workers,
