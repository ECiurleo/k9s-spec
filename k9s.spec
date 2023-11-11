Name:           k9s
Version:        0.28.1
Release:        1%{?dist}
Summary:        Kubernetes CLI To Manage Your Clusters In Style!
License:        Apache-2.0
URL:            https://k9scli.io/
Source0:        https://github.com/derailed/k9s/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  make, git, go, wget, bsdtar, binutils, libX11-devel, jq

%if 0%{?suse_version:1}
# -gold provides ld
BuildRequires: binutils-gold
%endif

# there's no debug files in this build
%define debug_package %{nil}

%description
K9s provides a terminal UI to interact with your Kubernetes clusters. The aim of this project is to make it easier to navigate, observe and manage your applications in the wild. K9s continually watches Kubernetes for changes and offers subsequent commands to interact with your observed resources.

%prep
%autosetup -n %{name}-%{version}

# make sure we're using the developer required version
# useful when building in system that have an older go version
REQUIRED_GO_VERSION=$(grep -oP '^go \K(0|[1-9]\d*\.(0|[1-9]\d*))$' go.mod)
echo "Target go version: $REQUIRED_GO_VERSION - %{_arch}"


PATCH_GO_VERSION=$(curl "https://go.dev/dl/?mode=json" | jq -r ".[] | select(.version | startswith(\"go${REQUIRED_GO_VERSION}\")) | .version")
echo "Ensuring minimal go version $PATCH_GO_VERSION"

# %{ix86}
%ifarch i386 i486 i586 i686 pentium3 pentium4 athlon geode
ARCH=386
%endif

# %{arm}
%ifarch armv3l armv4b armv4l armv4tl armv5tl armv5tel armv5tejl armv6l armv6hl armv7l armv7hl armv7hnl armv8l armv8hl armv8hnl armv8hcnl
ARCH=armv6l
%endif

# %{arm64}
%ifarch aarch64
ARCH=arm64
%endif

%ifarch x86_64
ARCH=amd64
%endif

wget https://go.dev/dl/${PATCH_GO_VERSION}.linux-${ARCH}.tar.gz
echo $PWD
ls
tar xzf $PATCH_GO_VERSION.linux-${ARCH}.tar.gz


%build
export PATH=$PWD/go/bin:$PATH
go version
make %{?_smp_mflags} build

%install
install -D -m 0755 %{_builddir}/%{name}-%{version}/execs/%{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
* Sun Nov 11 2023 Emanuele Ciurleo <emanuele@ciurleo.com> - %{version}
- Build of version %{version} - changes here https://github.com/derailed/k9s/releases/tag/v%{version}
* Tue Nov 07 2023 Emanuele Ciurleo <emanuele@ciurleo.com> - 0.28.0
- Build of version 0.28.0 - changes here https://github.com/derailed/k9s/releases/tag/v0.28.0 
* Mon Aug 28 2023 Emanuele Ciurleo <emanuele@ciurleo.com> - 0.27.4
- Build of version 0.27.4 - changes here https://github.com/derailed/k9s/releases/tag/v0.27.4 
