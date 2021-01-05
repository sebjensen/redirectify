def makeRedirect(name, site, title, url, description, img):
  html = f"""
  <html>
  <head>
    <meta http-equiv="refresh" content="0; url={url}">
    <script type="text/javascript">
      window.location.href = "{url}"
    </script>
    <title>{title}</title>
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:site" content="{site}" />
    <meta name="twitter:title" content="{site}" />
    <meta name="twitter:description" content="{description}" content="{img}" />
  </head>
  <body>
    If you are not redirected automatically, follow this <a href='{url}'>link</a>.
  </body>
  </html>
  """
  try:
    htmlPage = open(f"redirects/{name}.html","w+")
    htmlPage.write(html)
  except FileNotFoundError:
    print("Please ensure that a directory named 'redirects' exists and try again.")

while 1 == 1:
  url = input("Redirects to (URL): ")
  name = input("Redirects from (file name, exclude .html): ") # Don't include .html, if on a website it would be example.com/redirectname
  title = input("Title: ") # Used for Open Graph Meta Tags and HTML title tags
  site = input("Site Name (owner/category): ") # Used for Open Graph Meta Tags, the site/category that the link being redirected to falls under
  description = input("Description: ") # Used for Open Graph Meta Tags
  img = input("Image URL: ") # Used for Open Graph Meta Tags
  makeRedirect(name, site, title, url, description, img)
  print(f"Redirect created successfully at redirects/{name}.html\n")
