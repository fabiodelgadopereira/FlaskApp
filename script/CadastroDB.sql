USE [master]
GO
/****** Object:  Database [CadastroDB]    Script Date: 05-May-19 7:19:30 PM ******/
CREATE DATABASE [CadastroDB]

ALTER DATABASE [CadastroDB] SET COMPATIBILITY_LEVEL = 140
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [CadastroDB].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [CadastroDB] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [CadastroDB] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [CadastroDB] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [CadastroDB] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [CadastroDB] SET ARITHABORT OFF 
GO
ALTER DATABASE [CadastroDB] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [CadastroDB] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [CadastroDB] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [CadastroDB] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [CadastroDB] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [CadastroDB] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [CadastroDB] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [CadastroDB] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [CadastroDB] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [CadastroDB] SET  DISABLE_BROKER 
GO
ALTER DATABASE [CadastroDB] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [CadastroDB] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [CadastroDB] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [CadastroDB] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [CadastroDB] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [CadastroDB] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [CadastroDB] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [CadastroDB] SET RECOVERY FULL 
GO
ALTER DATABASE [CadastroDB] SET  MULTI_USER 
GO
ALTER DATABASE [CadastroDB] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [CadastroDB] SET DB_CHAINING OFF 
GO
ALTER DATABASE [CadastroDB] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [CadastroDB] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [CadastroDB] SET DELAYED_DURABILITY = DISABLED 
GO
EXEC sys.sp_db_vardecimal_storage_format N'CadastroDB', N'ON'
GO
ALTER DATABASE [CadastroDB] SET QUERY_STORE = OFF
GO
USE [CadastroDB]
GO
ALTER DATABASE SCOPED CONFIGURATION SET IDENTITY_CACHE = ON;
GO
ALTER DATABASE SCOPED CONFIGURATION SET LEGACY_CARDINALITY_ESTIMATION = OFF;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET LEGACY_CARDINALITY_ESTIMATION = PRIMARY;
GO
ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 0;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET MAXDOP = PRIMARY;
GO
ALTER DATABASE SCOPED CONFIGURATION SET PARAMETER_SNIFFING = ON;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET PARAMETER_SNIFFING = PRIMARY;
GO
ALTER DATABASE SCOPED CONFIGURATION SET QUERY_OPTIMIZER_HOTFIXES = OFF;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET QUERY_OPTIMIZER_HOTFIXES = PRIMARY;
GO
USE [CadastroDB]
GO
/****** Object:  Table [dbo].[Clientes]    Script Date: 05-May-19 7:19:30 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Clientes](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Nome] [nvarchar](80) NOT NULL,
	[Cidade] [nvarchar](50) NOT NULL,
	[Email] [nvarchar](80) NULL,
	[Sexo] [nvarchar](10) NOT NULL
 CONSTRAINT [PK_Clientes] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  StoredProcedure [dbo].[DeleteValue]    Script Date: 05-May-19 7:19:31 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_Clientes_DeleteValue]
	-- Add the parameters for the stored procedure here
	@Id int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	delete [dbo].[Clientes]
	where Id = @Id
END
GO
/****** Object:  StoredProcedure [dbo].[GetAllValues]    Script Date: 05-May-19 7:19:31 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_Clientes_GetAllValues]
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	Select Id, Nome,Cidade,Email,Sexo
	from [Clientes]
END
GO
/****** Object:  StoredProcedure [dbo].[GetValueById]    Script Date: 05-May-19 7:19:31 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_Clientes_GetValueById] 
	-- Add the parameters for the stored procedure here
	@Id int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT  Id, Nome,Cidade,Email,Sexo
	from [Clientes]
	where Id = @Id
END
GO
/****** Object:  StoredProcedure [dbo].[InsertValue]    Script Date: 05-May-19 7:19:31 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_Clientes_InsertValue] 
	-- Add the parameters for the stored procedure here
	@Nome nvarchar(80),
	@Cidade nvarchar(50),
	@Email nvarchar(80),
	@Sexo nvarchar(10)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	insert into [Clientes] ( Nome,Cidade,Email,Sexo)
	values ( @Nome,@Cidade,@Email,@Sexo)
END
GO
/****** Object:  StoredProcedure [dbo].[InsertValue]    Script Date: 05-May-19 7:19:31 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

GO
USE [master]
GO
EXEC sp_adduser 'delgado'

USE [CadastroDB]
GO
GRANT SELECT, INSERT, UPDATE, DELETE ON [CadastroDB].dbo.Clientes TO delgado
GRANT execute ON [CadastroDB].dbo.sp_Clientes_InsertValue TO delgado
GRANT execute ON [CadastroDB].dbo.sp_Clientes_GetValueById TO delgado
GRANT execute ON [CadastroDB].dbo.sp_Clientes_GetAllValues TO delgado
GRANT execute ON [CadastroDB].dbo.sp_Clientes_DeleteValue TO delgado
ALTER DATABASE [CadastroDB] SET  READ_WRITE 
GO