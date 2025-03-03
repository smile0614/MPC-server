## Installing Python
Make sure you have Python 3.6 or higher installed.

## Launching MCP server
Open terminal and go to the project folder.
Start the server with the
```bash
command:python file_finder.py
```

## Setting up Cline in VSCode

### Open the Cline settings file in VSCode
Windows: 
```bash
%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json
```
macOS: 
```bash
~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
```

Linux: 
```bash
~/.config/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
```

### Add MCP server configuration
```bash
{
    "mcpServers": {
        "file-finder-mcp": {
            "args": [],
            "command": "python",
            "autoApprove": [],
            "disabled": false
        }
    }
}
```

### Note
In this example we use Python directly, so we specify the command ``` python ```. If you have a different Python path, specify it.

## Restart VSCode to load the updated settings.

### Example Prompt for Testing
To test the MCP server, send a request from Cline to VSCode:
```bash
{
    "method": "find_files",
    "params": {
        "path_fragment": "example"
    }
}
```
This query searches for files that contain the word "example" in the path.