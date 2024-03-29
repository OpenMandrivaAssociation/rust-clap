%ifnarch %{armx}
%bcond_without check
%else
# Workaround for rust breakage on some tests on aarch64
%bcond_with check
%endif
%global debug_package %{nil}

%global crate clap

Name:           rust-%{crate}
Version:        2.33.3
Release:        2
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/clap
Source:         %{crates_source}
# Initial patched metadata
# * Exclude useless files
# * Update strsim to 0.9, https://github.com/clap-rs/clap/pull/1450
Patch0:         clap-fix-metadata.diff
Patch1:		clap-2.33.3-update-textwrap.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Simple to use, efficient, and full-featured Command Line Argument Parser.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT
%doc README.md CHANGELOG.md CONTRIBUTORS.md SPONSORS.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+ansi_term-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ansi_term-devel %{_description}

This package contains library source intended for building other packages
which use "ansi_term" feature of "%{crate}" crate.

%files       -n %{name}+ansi_term-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+atty-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+atty-devel %{_description}

This package contains library source intended for building other packages
which use "atty" feature of "%{crate}" crate.

%files       -n %{name}+atty-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+clippy-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+clippy-devel %{_description}

This package contains library source intended for building other packages
which use "clippy" feature of "%{crate}" crate.

%files       -n %{name}+clippy-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+color-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+color-devel %{_description}

This package contains library source intended for building other packages
which use "color" feature of "%{crate}" crate.

%files       -n %{name}+color-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-devel %{_description}

This package contains library source intended for building other packages
which use "debug" feature of "%{crate}" crate.

%files       -n %{name}+debug-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+doc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+doc-devel %{_description}

This package contains library source intended for building other packages
which use "doc" feature of "%{crate}" crate.

%files       -n %{name}+doc-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+lints-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lints-devel %{_description}

This package contains library source intended for building other packages
which use "lints" feature of "%{crate}" crate.

%files       -n %{name}+lints-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+no_cargo-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_cargo-devel %{_description}

This package contains library source intended for building other packages
which use "no_cargo" feature of "%{crate}" crate.

%files       -n %{name}+no_cargo-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+strsim-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+strsim-devel %{_description}

This package contains library source intended for building other packages
which use "strsim" feature of "%{crate}" crate.

%files       -n %{name}+strsim-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+suggestions-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+suggestions-devel %{_description}

This package contains library source intended for building other packages
which use "suggestions" feature of "%{crate}" crate.

%files       -n %{name}+suggestions-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+term_size-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+term_size-devel %{_description}

This package contains library source intended for building other packages
which use "term_size" feature of "%{crate}" crate.

%files       -n %{name}+term_size-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+vec_map-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+vec_map-devel %{_description}

This package contains library source intended for building other packages
which use "vec_map" feature of "%{crate}" crate.

%files       -n %{name}+vec_map-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+wrap_help-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wrap_help-devel %{_description}

This package contains library source intended for building other packages
which use "wrap_help" feature of "%{crate}" crate.

%files       -n %{name}+wrap_help-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+yaml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+yaml-devel %{_description}

This package contains library source intended for building other packages
which use "yaml" feature of "%{crate}" crate.

%files       -n %{name}+yaml-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+yaml-rust-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+yaml-rust-devel %{_description}

This package contains library source intended for building other packages
which use "yaml-rust" feature of "%{crate}" crate.

%files       -n %{name}+yaml-rust-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
