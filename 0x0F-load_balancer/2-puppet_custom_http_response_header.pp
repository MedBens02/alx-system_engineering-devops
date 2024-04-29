# Configure Nginx with custom HTTP response header and custom pages in Puppet

# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the HTML directory exists
file { '/etc/nginx/html':
  ensure => directory,
  require => Package['nginx'],
}

# Create the main index.html
file { '/etc/nginx/html/index.html':
  ensure  => present,
  content => "Hello World!\n",
  require => File['/etc/nginx/html'],
}

# Create the custom 404 page
file { '/etc/nginx/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page\n",
  require => File['/etc/nginx/html'],
}

# Configure Nginx server with a custom configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80;
    listen [::]:80 default_server;
    root /etc/nginx/html;
    index index.html index.htm;
    add_header X-Served-By \$hostname;

    location /redirect_me {
        return 301 https://github.com/MedBens02;
    }

    error_page 404 /404.html;
    location /404 {
        root /etc/nginx/html;
        internal;
    }
  }\n",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

