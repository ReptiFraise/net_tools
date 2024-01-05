import net_tools.export_nextcloud.withRequests as withRequests
import net_tools.export_nextcloud.fileExplorer as fileExplorer
import net_tools.__main__ as net_tools

def main(conf):
    file = fileExplorer.main(conf)
    withRequests.upload(file, conf)
    net_tools.main()

if __name__ == '__main__':
    main()