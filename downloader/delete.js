const fs = require('fs-extra');
const path = require('path');

function cleanDirectory(directory) {
    fs.readdir(directory, (err, files) => {
        if (err) {
            return console.error(`Unable to scan directory: ${err}`);
        }

        files.forEach(file => {
            const filePath = path.join(directory, file);

            fs.stat(filePath, (err, stat) => {
                if (err) {
                    return console.error(`Unable to stat file: ${err}`);
                }

                if (stat.isDirectory()) {
                    // Recursively clean child directories
                    cleanDirectory(filePath);
                } else if (path.extname(filePath) !== '.html') {
                    // Delete file if it is not a .html file
                    fs.remove(filePath, err => {
                        if (err) {
                            return console.error(`Unable to delete file: ${err}`);
                        }
                        console.log(`Deleted file: ${filePath}`);
                    });
                }
            });
        });
    });
}

// Replace 'your_directory_path' with the path of the directory you want to clean
const directoryPath = './scss/sass-lang.com';
cleanDirectory(directoryPath);
