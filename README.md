# Masonite Filesystem Helper

This package provides helper functions for filesystem operations. 
Basically acts as a simple wrapper around [Pyfilesystem](https://docs.pyfilesystem.org/).

## Constants

This package provides the following helper constants.

### Openers

Used in the Pyfilesystem `open_fs` function.
[https://docs.pyfilesystem.org/en/latest/openers.html](https://docs.pyfilesystem.org/en/latest/openers.html)


```python
from filesystem import openers
```

```python
OPERATING_SYSTEM = 'osfs://'
MEMORY = 'mem://'
```

### Paths

Contains the directory names of the default *Masonite* installation.

```python
from filesystem import paths
```

````python
ROOT = BASE_DIRECTORY
APP = '/app'
APP_HTTP = '/app/http'
APP_PROVIDERS = '/app/providers'
APP_HTTP_CONTROLLERS = '/app/http/controllers'
APP_HTTP_MIDDLEWARE = '/app/http/middleware'
BOOTSTRAP = '/bootstrap'
BOOTSTRAP_CACHE = '/bootstrap/cache'
CONFIG = '/config'
DATABASES = '/databases'
DATABASES_MIGRATIONS = '/databases/migrations'
RESOURCES = '/resources'
RESOURCES_TEMPLATES = '/resources/templates'
RESOURCES_SNIPPETS = '/resources/snippets'
ROUTES = '/routes'
STORAGE = '/storage'
STORAGE_COMPILED = '/storage/compiled'
STORAGE_STATIC = '/storage/static'
STORAGE_UPLOADS = '/storage/uploads'
TESTS = '/tests'
````

#### Root

Are the same constants but they include the `BASE_DIRECTORY` constant before the paths

```python
from filesystem.paths import root
```

## Load methods

These methods wraps around the [open_fs](https://docs.pyfilesystem.org/en/latest/openers.html?highlight=open_fs#opening-fs-urls)
function.

```python
from filesystem import load 
```

### Main Methods

#### os(path)

Will return a filesystem pointing to the operating system.
Uses the current dir as default path value.

#### mock()

Will return a filesystem pointing to an in memory system. 
Specially useful for *unit testing*.

#### fs(opener)

Will return a filesystem with the provided opener.

#### root()

Will return a filesystem to the `config.application.BASE_DIRECTORY` in the operating system.


### Mock Methods


The following methods utilize the [copy_fs](https://docs.pyfilesystem.org/en/latest/reference/copy.html?highlight=copy_structure#fs.copy.copy_fs)
function to clone a filesystem to an in memory one.

The optional walker param (the same as the *copy_fs* one) helps defining which files or directory clone.

```python
from filesystem.load import mock
```

#### root(walker=None)

This method will return an in memory filesystem with the 
same structure and files as the filesystem returned by `load.root()`


#### root_only_structure(walker=None)

This method will return an in memory filesystem with the 
same structure but no files as the filesystem returned by `load.root()`


## Example Usage

The *Pyfilesytem* object returned by the helper methods
could be used when a [Command](https://docs.masoniteproject.com/the-craft-command/creating-commands) needs to create or copy
files or directories.

In the following code two filesystems are being initialized.
One used for the app root directory and other for the package directory.

The `fs_app` will change depending on the `mock` variable passed
as an optional param.

```python
# ...
import filesystem
# ...

def handle(self):
        mock = self.option('mock')
        
        # Filesystem of the Application Root
        fs_app = filesystem.load.root()
        
        # Filesystem of the package directory
        fs_package = filesystem.load.os(package_directory)
        
        # If the mock option is enabled we
        # close the previous filesystem and
        # use an in memory one for unit testing
        if mock:
            fs_app.close()
            fs_app = filesystem.load.mock()
         
         # ...
```

The following code will copy files from one file system
to another. If the directory does not exists then it 
will create one. Finally will only copy files if the are 
not present. Uses the [copy_file](https://docs.pyfilesystem.org/en/latest/reference/copy.html?highlight=copy_file#fs.copy.copy_file)
function.

```python
# ...
from fs.copy import copy_file
# ...
path = '/resources/lang/default/'

if not self.fs_app.exists(path):
    fs_lang = self.fs_app.makedirs(path)
else:
    fs_lang = self.fs_app.opendir(path)

if fs_lang.isempty('.'):

    filename = '__init__.py'

    copy_file(
        src_fs=self.fs_package,
        src_path='/snippets/resources/lang/default/' + filename,
        dst_fs=fs_lang,
        dst_path=filename
    )

fs_lang.close()
# ...
```

Made with <i>&#9829;</i> by <a href="https://ninjas.cl" target="_blank">Ninjas.cl</a>.
