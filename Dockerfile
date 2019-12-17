FROM mysql:5.7.21
COPY datainit.sh /
CMD ["/bin/bash"]
MAINTAINER dagon0577 dagon0577@gmail.com
EXPOSE 3306