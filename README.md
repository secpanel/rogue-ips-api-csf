rogue-ips-api-csf
=================

Collection of python source code which, implements a lifetime* free Rogue IPs API service for CSF users.

this method of using this API share some information from your server, which are not much senstive
such as :

<ul>
  <li> System Information (OS, Distro, RAM, CPU etc.) </li>
  <li> Banned IP Address </li>
<ul>

if you modify thr script such that no such sharing occurs API server which maintains a reputation for your server
will start decreasing your reputation and will eventually stop the service temporarily, until sharing becomes available
again.

Installation
============

Please follow the following steps for installating this service

<ol>
	<li>
		Dowload the collection scripts, also available at https://apis.secpanel.com/csf/downloads/csf-0.1.1.tar
		a wget can be done as :
		<pre>
			wget https://apis.secpanel.com/csf/downloads/csf-0.1.1.tar
		</pre>
        </li>
	<li>
		Make run.py an executable by giving it executable permission can also be done as :
		<pre>
			chmod +x run.py
		</pre>
	</li>
	<li>
		Make it a daily cron job
		<pre>
			cp run.py /etc/cron.daily/
			cp functions.py /etc/cron.daily/ 
		</pre>
		Note: Don't make hourly or more extensive cron job, pulling much data from the API server decreases reputation
	</li>
</ol>

* Please refer to Legal & Terms of Use @ https://apis.secpanel.com/legal.php  
